from django.urls import path
from .views import item_detail, buy_item, index, order_create

app_name = 'items'

urlpatterns = [
    path('', index, name='index'),
    path('order/', order_create, name='order_create'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('buy/<int:item_id>/', buy_item, name='buy_item')
]
