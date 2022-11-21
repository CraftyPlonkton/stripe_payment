from django import forms

from .models import Item, Order


class OrderMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, item):
        return f'{item.name} цена: {item.price} {item.currency}'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('items', 'discount', 'tax')
    items = OrderMMCF(
        queryset=Item.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
