from django.shortcuts import render

from rest_framework.generics import ListAPIView , RetrieveAPIView
from items.models import Item
from .serializers import ItemListSerializer , DetailListSerializer
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class ListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer 
    filter_backends = [OrderingFilter,]
    permission_classes = [AllowAny]


class DetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = DetailListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id' 
    permission_classes = [IsAuthenticated, IsAdminUser]



		


    