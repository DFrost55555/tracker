from django.shortcuts import render, redirect

def home(request):
    return render(request, 'main/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})

def products(request):
    return render(request, '../products/prod_home.html', {'title': 'Products'})