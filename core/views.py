from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from users.authentication_mixins import Authentication



class Index(TemplateView):

    template_name = "index.html"
    

class Home(Authentication, TemplateView):

    template_name = "home.html"


class Profile(Authentication, TemplateView):

    template_name = "profile.html"
    