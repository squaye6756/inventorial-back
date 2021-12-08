# Create your views here.
from rest_framework import generics
from .serializers import StoreSerializer
from .models import Store

class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all().order_by('id')
    serializer_class = StoreSerializer

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all().order_by('id')
    serializer_class = StoreSerializer
