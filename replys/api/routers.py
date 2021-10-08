from rest_framework.routers import DefaultRouter
from replys.api.views.replys_viewsets import ReplyViewSet


router = DefaultRouter()
router.register(r'replys', ReplyViewSet, basename='replys')

urlpatterns = router.urls