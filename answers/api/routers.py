from rest_framework.routers import DefaultRouter
from answers.api.views.answers_viewsets import AnswerViewSet


router = DefaultRouter()
router.register(r'answers', AnswerViewSet, basename='answers')

urlpatterns = router.urls