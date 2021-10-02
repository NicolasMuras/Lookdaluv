from rest_framework.routers import DefaultRouter
from cards.api.views.card_viewsets import CardViewSet
from cards.api.views.general_views import ModuleViewSet


router = DefaultRouter()
router.register(r'cards', CardViewSet, basename='cards')
router.register(r'modules', ModuleViewSet, basename='modules')

urlpatterns = router.urls