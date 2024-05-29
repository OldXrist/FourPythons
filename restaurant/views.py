from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BookingForm, LoginForm, RegisterForm
from .models import Menu, CartItem, Order, OrderDetail


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views


def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 


def admin(request):
    return render(request, 'admin.html')


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.username = form.username.lower()
            form.save()
            messages.success(request, 'You have singed up successfully.')
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})


def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username.title()}!')
                return redirect('home')

        # form is not valid or user is not authenticated
        messages.error(request, f'Некорректное имя пользователя или пароль!')
        return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return render(request, 'index.html')


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, product_id):
    product = Menu.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product,
                                                        user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('menu')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')


def order_create(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        address = request.POST['address']

        order, created = Order.objects.get_or_create(user=request.user, total=total_price, address=address)
        order.save()

        for item in cart_items:
            order_detail, created = OrderDetail.objects.get_or_create(order=order, product=item.product, quantity=item.quantity)
            order_detail.save()

        cart_items.delete()

        messages.success(request, 'Ваш заказ принят!')
        return redirect('home')
    else:
        return redirect('home')


def account(request, username):
    orders = Order.objects.filter(user=request.user)
    cart = CartItem.objects.filter(user=request.user)

    context = {
        "orders": orders,
        "cart": cart,
    }

    return render(request, 'account.html', context)


def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    detail = OrderDetail.objects.filter(order=order)
    total_price = sum(item.product.price * item.quantity for item in detail)
    return render(request, 'order.html', {'detail': detail, 'total_price': total_price, 'order': order})
