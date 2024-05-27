from django.contrib import admin
from .models import Menu, CartItem, Booking


# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(CartItem)
