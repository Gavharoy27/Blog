from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .models import *


def home_view(request):
    if request.user.is_authenticated:
        mualliflar = Muallif.objects.filter(user=request.user)
        context = {
            'mualliflar': mualliflar,
        }
        return render(request, 'home.html', context)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        if request.POST.get('password1') != request.POST.get('password2') or request.POST.get('username') in User.objects.values_list('username', flat=True):
            return redirect('register')
        user = User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password1'),
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('register')
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        if user is not None:
            return redirect('home')
        return redirect('login')
    return render(request, 'login.html')


def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('login')


def blog_view(request):
    if request.user.is_authenticated:
        maqolalar = Maqola.objects.filter(muallif__user=request.user)
        context = {
            'maqolalalr': maqolalar
        }
        return render(request, 'blog.html', context)
    return redirect('login')


def m_matn_view(request):
    if request.user.is_authenticated:
        maqola = Maqola.objects.filter(muallif__user=request.user)
        context = {
            'maqola': maqola
        }
        return render(request, 'm_matn_view', context)
    return redirect('login')


def blog_add_view(request):
    if request.method == 'POST':
        muallif = Muallif.objects.all()
        if request.user.is_authenticated:
            Maqola.objects.filter(muallif__user=request.user).create(
            sarlavha = request.POST.get('sarlavha'),
            matn = request.POST.get('matn'),
            mavzu = request.POST.get('mavzu'),
            muallif = muallif.last()
        )
            return redirect('home')
        return redirect('login')
    return render(request, 'blog_add.html')

