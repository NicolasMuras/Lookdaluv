"""amaterasu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

from users.api.views.users_views import Login, Logout
from core.views import index, home, profile
from users.views import Login, Logout



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('profile/<int:id>', profile),
    path('api/', include(('users.api.urls', 'users'))),
    path('api_generate_token/', views.obtain_auth_token),
    path('cards/', include('cards.api.urls')),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]