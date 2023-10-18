from django.shortcuts import render
from django.urls import include, path

def index(request):
    context = {
        'products': ['Товар 1', 'Товар 2', 'Товар 3'],
    }
    print(" ")
    print("кто то заходил на донаты")
    return render(request, 'donate/index.html', context)
