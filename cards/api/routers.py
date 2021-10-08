from rest_framework.routers import DefaultRouter
from cards.api.views.card_viewsets import CardViewSet


router = DefaultRouter()
router.register(r'cards', CardViewSet, basename='cards')

urlpatterns = router.urls