from django.urls import path

from cards.api.views.cards_views import CardListCreateAPIView, CardRetriveUpdateDestroyAPIView
from cards.api.views.general_views import ModuleListAPIView



urlpatterns = [
    path('card/', CardListCreateAPIView.as_view(), name='card'),
    path('card/<int:pk>/', CardRetriveUpdateDestroyAPIView.as_view(), name='card_detail'),
    path('module/', ModuleListAPIView.as_view(), name='module'),
]