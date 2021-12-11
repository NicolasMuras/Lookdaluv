from rest_framework.routers import DefaultRouter
from module_question.api.views.module_question_viewsets import QuestionModuleViewSet
from module_question.api.views.general_views import QuestionModuleStatisticsViewSet


router = DefaultRouter()
router.register(r'question_modules', QuestionModuleViewSet, basename='question-modules')
router.register(r'question_modules_statistics', QuestionModuleStatisticsViewSet, basename='question-modules-statistic')

urlpatterns = router.urls