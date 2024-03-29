# Generated by Django 4.1.6 on 2023-12-29 04:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_options'),
        ('products', '0007_alter_action_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Рейтинг')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'verbose_name_plural': 'Обратная связь',
            },
        ),
    ]
