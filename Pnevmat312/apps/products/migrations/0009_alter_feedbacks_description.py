# Generated by Django 4.1.6 on 2023-12-29 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_feedbacks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='description',
            field=models.TextField(max_length=2000, null=True, verbose_name='Описание'),
        ),
    ]