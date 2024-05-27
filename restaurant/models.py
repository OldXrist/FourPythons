from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Booking(models.Model):
    full_name = models.CharField('Имя', max_length=200)
    phone_number = models.IntegerField('Номер телефона', null=True)
    guest_number = models.IntegerField('Количество гостей')
    comment = models.CharField('Комментарий', max_length=1000)

    def __str__(self):
        return self.full_name


# Add code to create Menu model
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    menu_item_description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
