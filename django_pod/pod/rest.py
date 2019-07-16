# Serializers define the API representation.

from .models import SKU, Brand
from rest_framework import serializers, viewsets


class SKUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SKU
        fields = ['name', 'brand']


class SKUViewSet(viewsets.ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'contact']


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
