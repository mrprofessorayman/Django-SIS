from django.shortcuts import render


def home(request, guestname="Ayman"):
    return render(request, 'home.html', { "name": guestname})
