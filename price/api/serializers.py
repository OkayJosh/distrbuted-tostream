from rest_framework import serializers
from price.models import PriceIndex


class PriceIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceIndex
        fields = '__all__'
