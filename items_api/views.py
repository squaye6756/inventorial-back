# Create your views here.
from rest_framework import generics
from .serializers import ItemSerializer
from .models import Item

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all().order_by('name')
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all().order_by('name')
    serializer_class = ItemSerializer
