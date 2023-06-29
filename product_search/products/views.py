from rest_framework.views import APIView
from rest_framework.response import Response
from products.serializers import ProductSearchSerializer
from products.utils import authenticate


class ProductSearchView(APIView):
    def get(self, request):
        user_id = authenticate(request)
        serializer = ProductSearchSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        return Response("Product search results")
