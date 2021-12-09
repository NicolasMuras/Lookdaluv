from rest_framework.routers import DefaultRouter
from contents_chatbot.api.views.contents_chatbot_viewsets import InterviewSimulatorModuleViewSet
from contents_chatbot.api.views.general_views import InterviewSimulatorModuleStatisticsViewSet


router = DefaultRouter()
router.register(r'interview_simulator_modules', InterviewSimulatorModuleViewSet, basename='interview-simulator-modules')
router.register(r'interview_simulator_modules_statistics', InterviewSimulatorModuleStatisticsViewSet, basename='interview-simulator-modules-statistic')

urlpatterns = router.urls