from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from .models import Retsept,Product,Deliver
from .serializer import *



class RetseptAPIViewSet(viewsets.ModelViewSet):
    queryset =Retsept.objects.all()
    serializer_class = RetseptSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeliverViewSet(viewsets.ModelViewSet):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer
