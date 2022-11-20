from django.contrib import admin
from.models import Item, Discount, Tax, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'price', 'currency')
    search_fields = ('name',)

    def short_description(self, obj):
        return obj.description[:30]

    short_description.__name__ = 'Сокращенное описание'


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'value_percent')


class TaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'value_percent')


class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ('items',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Tax, TaxAdmin)
admin.site.register(Order, OrderAdmin)
