from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from core.api import GeneralListAPIView
from cards.api.serializers.cards_serializers import CardListCreateUpdateSerializer



class CardListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CardListCreateUpdateSerializer
    queryset = serializer_class.Meta.model.objects.filter(state=True)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '[+] Producto creado correctamente.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CardListCreateUpdateSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
        
    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            card_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(card_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':"Doesn't exist a card with that information."}, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        if self.get_queryset(pk):
            card_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if card_serializer.is_valid():
                card_serializer.save()
                return Response(card_serializer.data, status=status.HTTP_200_OK)
            return Response(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        card = self.get_queryset().filter(id=pk).first()
        if card:
            card.state = False
            card.save()
            return Response({'message':'Tarjeta eliminada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error':"Doesn't exist a card with that information."}, status=status.HTTP_400_BAD_REQUEST)
