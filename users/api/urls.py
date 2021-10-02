from django.urls import path
from users.api.views.users_views import UserList

urlpatterns = [
    path('user/', UserList.as_view(), name='user_list'),
]