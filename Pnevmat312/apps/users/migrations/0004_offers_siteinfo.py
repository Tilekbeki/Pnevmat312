# Generated by Django 4.1.6 on 2024-01-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='actions_img', verbose_name='Изображение предdddddddложения')),
                ('link', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name_plural': 'Предложения',
            },
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guaranteesText', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание страницы гарантии')),
                ('descriptionSite', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание сайта')),
                ('payText', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание страницы оплаты')),
            ],
            options={
                'verbose_name_plural': 'Информация',
            },
        ),
    ]
