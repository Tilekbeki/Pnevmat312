# Generated by Django 4.1.6 on 2024-01-07 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_feedbacks_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='date_published',
            field=models.DateField(default=datetime.datetime(2024, 1, 17, 20, 5, 41, 872794), verbose_name='Дата публикации'),
        ),
    ]
