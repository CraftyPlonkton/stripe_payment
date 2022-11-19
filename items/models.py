from django.core.validators import MaxValueValidator
from django.db import models


class Item(models.Model):
    CURRENCY_CHOICES = [
        ('usd', 'United States dollar'),
        ('rub', 'Russian ruble')
    ]
    name = models.CharField(
        max_length=256,
        verbose_name='Наименование',
        help_text='Введите наименование товара'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание товара'
    )
    price = models.FloatField(
        verbose_name='Цена',
        help_text='Введите цену товара'
    )
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='rub',
        verbose_name='Валюта',
        help_text='Выберите валюту'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=256, unique=True)
    value_percent = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=256, unique=True)
    value_percent = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(
        Item,
        verbose_name='Товар',
        help_text='Выберите товар',
        related_name='order'
    )
    discount = models.ForeignKey(
        Discount,
        default=None,
        verbose_name='Скидка',
        help_text='Выберите скидку',
        related_name='order',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True
    )
    tax = models.ForeignKey(
        Tax,
        default=None,
        verbose_name='Налог',
        help_text='Выберите налоговую ставку',
        related_name='order',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True
    )
