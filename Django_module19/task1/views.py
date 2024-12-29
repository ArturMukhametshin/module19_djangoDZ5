from django.shortcuts import render
from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def cart(request):

    return render(request, 'first_task/cart.html')

def games(request):
    title_g = 'Игры'
    games = Game.objects.all()
    context = {
        'games': games,
        'title_g': title_g
    }
    return render(request, 'first_task/games.html', context)

def platform(request):
    title_p = 'Корзина'
    message = 'Извините, ваша корзина пуста'
    context = {
        'title_p': title_p,
        'message': message
    }

    return render(request, 'first_task/platform.html', context)

def menu(request):
    general = 'Главная страница'
    shop = 'Магазин'
    products = 'Корзина'
    context = {
        'general': general,
        'shop': shop,
        'products': products
    }
    return render(request, 'first_task/menu.html', context)

def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    users_list = []
    for user in users:
        users_list.append(user.name)
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']


            if password == repeat_password and int(age) > 18 and username not in users_list:
                users.create(name=username,balance=0, age=age)
                info['message'] = f'Приветсвуем, {username}'
                form = UserRegister
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18 лет'
            elif username in users_list:
                info['error'] = 'Пользователь уже существует'
        info['form'] = form
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'first_task/registration_page.html', info)

def news(request):
    post = News.objects.all()
    paginator = Paginator(post, 3)
    num_pages = request.GET.get('page')
    news = paginator.get_page(num_pages)
    return render(request, 'first_task/news.html', {'news': news})

