# Generated by Django 4.1.6 on 2023-12-29 05:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_order_date_created_alter_order_date_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 12, 8, 37, 325580), verbose_name='Дата создания корзины'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 8, 12, 8, 37, 325580), verbose_name='Дата доставки'),
        ),
    ]
