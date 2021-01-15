from price.models import PriceIndex
from .serializers import PriceIndexSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter


class PriceIndexViewset(ModelViewSet):
    serializer_class = PriceIndexSerializer
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['name', 'price']
    queryset = PriceIndex.objects.all()