from rest_framework import serializers

from .models import Retsept,Product,Deliver

class RetseptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retsept
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class DeliverSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Deliver
        fields = "__all__"
            