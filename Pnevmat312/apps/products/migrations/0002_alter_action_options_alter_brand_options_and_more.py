# Generated by Django 5.0 on 2023-12-12 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'verbose_name_plural': 'Акции'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': 'Бренды'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Свойства'},
        ),
        migrations.AlterModelOptions(
            name='sliders',
            options={'verbose_name_plural': 'Изображения'},
        ),
    ]