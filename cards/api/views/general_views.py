from rest_framework import generics

from core.api import GeneralListAPIView
from cards.api.serializers.generals_serializer import ModuleSerializer



class ModuleListAPIView(GeneralListAPIView):
    serializer_class = ModuleSerializer
