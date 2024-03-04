# Generated by Django 4.1.6 on 2024-01-05 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_order_ordertext_alter_order_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_delivery',
        ),
        migrations.AddField(
            model_name='order',
            name='date_executed',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 15, 17, 17, 46, 964400), verbose_name='Дата доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 17, 17, 46, 963401), verbose_name='Дата создания корзины'),
        ),
    ]
