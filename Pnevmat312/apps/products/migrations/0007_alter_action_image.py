# Generated by Django 4.1.6 on 2023-12-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_mainpagesliders_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='actions_img', verbose_name='Изображение профиля'),
        ),
    ]
