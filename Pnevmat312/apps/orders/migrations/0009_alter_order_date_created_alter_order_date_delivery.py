# Generated by Django 4.1.6 on 2023-12-28 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_date_created_alter_order_date_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 28, 23, 20, 2, 838093), verbose_name='Дата создания корзины'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 23, 20, 2, 838093), verbose_name='Дата доставки'),
        ),
    ]