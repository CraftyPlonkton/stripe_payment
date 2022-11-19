import stripe
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Item
from .forms import OrderForm

# TODO убрать в енв
stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'


def index(request):
    template = 'index.html'
    return render(request, template)


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
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name
                },
                'unit_amount_decimal': item.price * 100
            },
            'quantity': 1
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('items:index')),
        cancel_url=request.build_absolute_uri(reverse('items:index'))
    )
    return redirect(session.url, code=303)
