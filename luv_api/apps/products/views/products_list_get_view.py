from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ..serializers import ProductSerializer

from ..models import  Product
from ..renderers import ProductJSONRenderer

class ProductsListGetView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    queryset = Product.objects
    renderer_classes = (ProductJSONRenderer,)


    def list(self, request):

        serializer = self.get_serializer(self.queryset.all(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
