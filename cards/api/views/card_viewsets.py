from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from cards.api.serializers.cards_serializers import CardSerializer
from users.authentication_mixins import Authentication



class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        card_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(card_serializer.data, status=status.HTTP_200_OK)
            
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '[+] Card created successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            card_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if card_serializer.is_valid():
                card_serializer.save()
                return Response(card_serializer.data, status=status.HTTP_200_OK)
            return Response(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'[!] System error.'}, status=status.HTTP_502_BAD_GATEWAY)

    def destroy(self, request, pk=None):
        card = self.get_queryset().filter(id=pk).first()
        if card:
            card.state = False
            card.save()
            return Response({'message':'[*] Card deleted successfully.'}, status=status.HTTP_200_OK)
        return Response({'error':"[!] Doesn't exist a card with that information."}, status=status.HTTP_400_BAD_REQUEST)
