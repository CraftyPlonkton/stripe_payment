from django.contrib import admin
from.models import Item, Discount, Tax, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'price', 'currency')
    search_fields = ('name',)

    def short_description(self, obj):
        return obj.description[:30]

    short_description.__name__ = 'Сокращенное описание'


admin.site.register(Item, ItemAdmin)
admin.site.register(Discount)
admin.site.register(Tax)
admin.site.register(Order)
