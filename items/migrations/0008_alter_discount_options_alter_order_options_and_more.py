# Generated by Django 4.1.3 on 2022-11-20 19:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_alter_order_discount_alter_order_tax'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'verbose_name': 'Скидка', 'verbose_name_plural': 'Скидки'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='tax',
            options={'verbose_name': 'Налог', 'verbose_name_plural': 'Налоги'},
        ),
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=models.CharField(help_text='Введите название скидки', max_length=256, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='value_percent',
            field=models.PositiveSmallIntegerField(help_text='Введите значение в %', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Значение'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='name',
            field=models.CharField(help_text='Введите название налога', max_length=256, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='value_percent',
            field=models.PositiveSmallIntegerField(help_text='Введите значение в %', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Значение'),
        ),
    ]