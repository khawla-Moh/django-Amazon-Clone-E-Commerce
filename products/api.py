from rest_framework import generics
from .models import Product,Brand,Reviews,ProductImages
from . import serializers


class ProductListAPI(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=serializers.ProductListSerializer


class ProductDetailAPI(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=serializers.ProductDetailSerializer    



class BrandListAPI(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=serializers.BrandListSerializer    


class BrandDetailAPI(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=serializers.BrandDetailSerializer    