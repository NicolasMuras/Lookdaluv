from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm

def index(request):
    views = 5

    context = {
        'views': views,
    }

    return render(request, 'index.html', context)

def home(request):
    views = 5

    context = {
        'views': views,
    }
    return render(request, 'home.html', context)

def profile(request, id):

    return HttpResponse("ID: {}".format(id))

def user_dashboard(request, id):

    return HttpResponse("DASHBOARD for ID: {}".format(id))