from rest_framework.routers import DefaultRouter

from users.api.views.general_views import ProfileViewSet


router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profiles')


urlpatterns = router.urls