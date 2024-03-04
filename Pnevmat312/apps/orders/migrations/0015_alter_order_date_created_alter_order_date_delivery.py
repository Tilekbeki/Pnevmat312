# Generated by Django 4.1.6 on 2023-12-29 05:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_alter_order_date_created_alter_order_date_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 12, 19, 56, 509665), verbose_name='Дата создания корзины'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 8, 12, 19, 56, 509665), verbose_name='Дата доставки'),
        ),
    ]
