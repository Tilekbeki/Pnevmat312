from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
import datetime



class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Категории'

    name = models.TextField('Название категории', max_length=1000)

    def __str__(self):
        return self.name


class Brand(models.Model):
    class Meta:
        verbose_name_plural = 'Бренды'

    name = models.TextField('Название бренда', max_length=100)
    image = models.ImageField('Изображение бренда', upload_to='brand_img', blank=True, null=True)
    description = models.TextField('Описание', max_length=2000)
    def __str__(self):
        return self.name


class Product(models.Model):
    RECOMENDED = 'RE'
    NEW = 'NE'
    SALEON = 'SA'
    TYPE_CHOICES = [
        (RECOMENDED, 'Рекомендуемые'),
        (NEW, 'Новинки'),
        (SALEON, 'Распродажа'),
    ]

    class Meta:
        verbose_name_plural = 'Продукты'

    name = models.TextField('Название продукта', max_length=1000)
    video = models.TextField('Ссылка на видео', max_length=1000, null=True, blank=True)
    price = models.IntegerField('Цена')
    quantity = models.IntegerField('Количество на складе')
    description = models.TextField('Описание', max_length=2000)
    type = models.CharField('Тип', max_length=2, choices=TYPE_CHOICES, default=NEW)
    id_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    id_brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} - {self.id_brand.name}"


class Action(models.Model):
    class Meta:
        verbose_name_plural = 'Акции'

    title = models.TextField(max_length=1000)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    date_published = models.DateTimeField('Дата начала')
    deadline = models.DateTimeField('Окончание')
    link = models.TextField(max_length=1000)
    image = models.ImageField('Изображение акции', upload_to='actions_img', blank=True, null=True)

    def __str__(self):
        return self.title


class Property(models.Model):
    class Meta:
        verbose_name_plural = 'Свойства'

    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.TextField(max_length=1000)
    value = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.id_product.name} - {self.name}"


class Sliders(models.Model):
    class Meta:
        verbose_name_plural = 'Изображения'

    image = models.ImageField('Изображение профиля', upload_to='products_sliders', blank=True, null=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_product.name}"


class MainPageSliders(models.Model):
    class Meta:
        verbose_name_plural = 'Изображения Главная страница'

    image = models.ImageField('Изображение', upload_to='main_page_sliders', blank=True, null=True)

    def __str__(self):
        return f"Изображение"


class FeedBacks(models.Model):
    class Meta:
        verbose_name_plural = 'Обратная связь'

    id_user = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField('Рейтинг', validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.TextField('Описание', max_length=2000, null=True, blank=True)
    date_published = models.DateField('Дата публикации', default=(datetime.datetime.today()
                                                                   + datetime.timedelta(days=10)))



    def __str__(self):
        return f"{self.id_product.name}"



