# Generated by Django 5.0 on 2023-12-05 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, verbose_name='Название бренда')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1000, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1000, verbose_name='Название продукта')),
                ('video', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Ссылка на видео')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Количество на складе')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('id_brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.brand')),
                ('id_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=1000)),
                ('description', models.TextField(max_length=1000)),
                ('date_published', models.DateTimeField(verbose_name='Дата начала')),
                ('deadline', models.DateTimeField(verbose_name='Окончание')),
                ('link', models.TextField(max_length=1000)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1000)),
                ('value', models.TextField(max_length=1000)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products_sliders', verbose_name='Изображение профиля')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]