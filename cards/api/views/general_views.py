from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from cards.models import Module
from core.api import GeneralListAPIView
from cards.api.serializers.generals_serializer import ModuleSerializer



class ModuleViewSet(viewsets.GenericViewSet):
    model = Module
    serializer_class = ModuleSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        module_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(module_serializer.data, status=status.HTTP_200_OK)
