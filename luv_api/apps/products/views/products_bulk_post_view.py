
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ..serializers import ProductSerializer



class ProductsBulkPostView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    def create(self, request):
        is_many = True if isinstance(request.data.get('products'), list) else False

        serializer = self.get_serializer(data=request.data.get('products', []), many=is_many)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
