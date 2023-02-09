import os
from typing import Optional

import stripe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from dotenv import load_dotenv
from stripe.error import StripeError

from .forms import OrderForm
from .models import Item, Order

load_dotenv()
stripe.api_key = os.getenv(
    'STRIPE_API_KEY', default='sk_test_4eC39HqLyjWDarjtT1zdp7dc'
)


def create_line_items(item: Item, tax_id: Optional[str] = None) -> dict:
    line_items = {
        'price_data': {
            'currency': item.currency,
            'product_data': {
                'name': item.name
            },
            'unit_amount_decimal': item.price * 100
        },
        'quantity': 1,
        'adjustable_quantity': {
            'enabled': True, 'maximum': 999, 'minimum': 1
        }
    }
    if tax_id:
        line_items.update({'tax_rates': [tax_id]})
    return line_items


def add_session_settings(
        line_items: list, request, coupon_id: Optional[str] = None) -> dict:
    data = {
        'line_items': line_items,
        'mode': 'payment',
        'discounts': [{'coupon': coupon_id}],
        'success_url': request.build_absolute_uri(reverse('items:index')),
        'cancel_url': request.build_absolute_uri(reverse('items:index'))
    }
    return data


def index(request):
    items = Item.objects.all()
    template = 'index.html'
    context = {'items': items}
    return render(request, template, context)


def error_page(request):
    template = 'error_page.html'
    context = {'error': request.session.get('error')}
    return render(request, template, context)


def item_detail(request, item_id):
    template = 'item_detail.html'
    item = get_object_or_404(Item, id=item_id)
    context = {'item': item}
    return render(request, template, context)


def order_create(request):
    template = 'order.html'
    form = OrderForm(request.POST or None)
    if not form.is_valid():
        return render(request, template, {'form': form})
    order = form.save()
    return redirect('items:buy_order', order.id)


def buy_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    line_items = [create_line_items(item)]
    line_items = add_session_settings(line_items, request)
    try:
        session = stripe.checkout.Session.create(**line_items)
        return JsonResponse(session)
    except StripeError as error:
        request.session['error'] = error.user_message
        return redirect('items:error_page')


def buy_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    items = order.items.all()
    coupon = order.discount
    tax = order.tax
    if coupon:
        coupon = stripe.Coupon.create(
            percent_off=coupon.value_percent, duration="once"
        ).get('id')
    if tax:
        tax = stripe.TaxRate.create(
            display_name='Tax', inclusive=False, percentage=tax.value_percent
        ).get('id')
    line_items = [create_line_items(item, tax) for item in items]
    line_items = add_session_settings(line_items, request, coupon)
    try:
        session = stripe.checkout.Session.create(**line_items)
        return redirect(session.url, code=303)
    except StripeError as error:
        request.session['error'] = error.user_message
        return redirect('items:error_page')
