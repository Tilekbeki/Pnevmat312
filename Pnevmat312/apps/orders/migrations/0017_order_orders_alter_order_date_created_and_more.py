# Generated by Django 4.1.6 on 2023-12-29 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_alter_order_date_created_alter_order_date_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orders',
            field=models.TextField(default='', max_length=1000, verbose_name='Товары из корзины'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 1, 3, 9, 988223), verbose_name='Дата создания корзины'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 1, 3, 9, 988223), verbose_name='Дата доставки'),
        ),
    ]
