import datetime
from django.db import models


class Order(models.Model):
    class Meta:
        verbose_name_plural = 'Заказы'

    date_created = models.DateTimeField('Дата создания корзины', default=datetime.datetime.today())
    date_executed = models.DateTimeField('Дата Исполнения', default=(datetime.datetime.today()
                                                                   + datetime.timedelta(days=10)))
    id_user = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    address = models.TextField('Номер телефона', max_length=1000)
    placed = models.BooleanField('Оформлено', default=False)
    orderText = models.TextField('Товары', max_length=1000)
    executed = models.BooleanField('Исполнено', default=False)
    def delete_order(self):
        self.delete()
    def __str__(self):
        return f"{self.id_user.profile.username} {self.address}"


class Cart(models.Model):
    class Meta:
        verbose_name_plural = 'Корзины'

    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id_product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField('Количество')

    def delete_cart(self):
        self.delete()

    def __str__(self):
        return f"{self.id_order.id_user.profile.username} - {self.id_product.name} - {self.quantity} шт"