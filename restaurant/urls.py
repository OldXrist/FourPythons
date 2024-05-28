from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"), 
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('register/', views.register, name="register"),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('order-create/', views.order_create, name='order_create'),
    path('account/<str:username>', views.account, name='account'),
    path('orders/<int:order_id>', views.order_detail, name="order_detail")
]
