from rest_framework.routers import DefaultRouter
from contents_chatbot.api.views.contents_chatbot_viewsets import ChatbotModuleViewSet
from contents_chatbot.api.views.general_views import ChatbotModuleStatisticsViewSet


router = DefaultRouter()
router.register(r'chatbot_modules', ChatbotModuleViewSet, basename='chatbot-modules')
router.register(r'chatbot_modules_statistics', ChatbotModuleStatisticsViewSet, basename='chatbot-modules-statistic')

urlpatterns = router.urls