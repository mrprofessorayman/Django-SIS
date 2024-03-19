from django.shortcuts import render


def home(request):
    myname = "Ayman"
    return render(request, 'home.html', { "name": myname})
