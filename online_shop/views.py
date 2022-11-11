from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @action(detail=True, methods=['GET'], name='products', url_path='products')
    def get_product(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = ProductSerializer(category.title.all(), many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()







