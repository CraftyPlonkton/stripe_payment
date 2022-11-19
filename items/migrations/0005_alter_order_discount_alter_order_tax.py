# Generated by Django 4.1.3 on 2022-11-19 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_order_discount_alter_order_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(default=0, help_text='Выберите скидку', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='order', to='items.discount', verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tax',
            field=models.ForeignKey(default=0, help_text='Выберите налоговую ставку', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='order', to='items.tax', verbose_name='Налог'),
        ),
    ]
