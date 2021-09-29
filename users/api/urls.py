from django.urls import path
from users.api.views.users_views import AccountList

urlpatterns = [
    path('account/', AccountList.as_view(), name='account_list'),
]