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
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Название',
        help_text='Введите название скидки'
    )
    value_percent = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100)],
        verbose_name='Значение %',
        help_text='Введите значение в %'
    )

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f'{self.name}: {self.value_percent}%'


class Tax(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Название',
        help_text='Введите название налога'
    )
    value_percent = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100)],
        verbose_name='Значение %',
        help_text='Введите значение в %'
    )

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'

    def __str__(self):
        return f'{self.name}: {self.value_percent}%'


class Order(models.Model):
    items = models.ManyToManyField(
        Item,
        related_name='order',
        verbose_name='Товар',
        help_text='Выберите товар'
    )
    discount = models.ForeignKey(
        Discount,
        default=None,
        related_name='order',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        verbose_name='Скидка',
        help_text='Выберите скидку'
    )
    tax = models.ForeignKey(
        Tax,
        default=None,
        related_name='order',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        verbose_name='Налог',
        help_text='Выберите налоговую ставку'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ ID: {self.id}'
