from django.shortcuts import render


def home(request):
    return render(request, 'manga/home.html')
