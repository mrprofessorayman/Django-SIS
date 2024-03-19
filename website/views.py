from django.shortcuts import render


def home(request, guestname):
    myname = "Ayman"
    return render(request, 'home.html', { "name": guestname})
