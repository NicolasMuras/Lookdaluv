from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from users.authentication_mixins import Authentication



class GeneralViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '[+] {} created successfully.'.format(self.model_to_format)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'[!] System error.'}, status=status.HTTP_502_BAD_GATEWAY)

    def destroy(self, request, pk=None):
        item = self.get_queryset().filter(id=pk).first()
        if item:
            item.state = False
            item.save()
            return Response({'message':'[*] {} deleted successfully.'.format(self.model_to_format)}, status=status.HTTP_200_OK)
        return Response({'error':"[!] Doesn't exist a {} with that information.".format(self.model_to_format)}, status=status.HTTP_400_BAD_REQUEST)