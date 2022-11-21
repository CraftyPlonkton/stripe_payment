from django.urls import path

from .views import (buy_item, buy_order, error_page, index, item_detail,
                    order_create)

app_name = 'items'

urlpatterns = [
    path('', index, name='index'),
    path('error/', error_page, name='error_page'),
    path('order/', order_create, name='order_create'),
    path('order/<int:order_id>/', buy_order, name='buy_order'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('buy/<int:item_id>/', buy_item, name='buy_item')
]
