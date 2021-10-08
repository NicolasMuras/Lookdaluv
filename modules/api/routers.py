from rest_framework.routers import DefaultRouter
from modules.api.views.modules_viewsets import ModuleViewSet
from modules.api.views.general_views import GeneralViewSet


router = DefaultRouter()
router.register(r'modules', ModuleViewSet, basename='modules')


urlpatterns = router.urls