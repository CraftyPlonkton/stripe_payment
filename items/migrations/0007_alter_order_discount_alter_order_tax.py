# Generated by Django 4.1.3 on 2022-11-19 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_order_discount_alter_order_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, default=None, help_text='Выберите скидку', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='order', to='items.discount', verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tax',
            field=models.ForeignKey(blank=True, default=None, help_text='Выберите налоговую ставку', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='order', to='items.tax', verbose_name='Налог'),
        ),
    ]
