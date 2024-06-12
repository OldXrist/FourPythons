from django.contrib import admin
from .models import Menu, CartItem, Booking, Order, OrderDetail, Review


# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Review)
