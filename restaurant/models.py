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