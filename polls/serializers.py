from rest_framework import serializers
from .models import Phones, Headphones

class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ('phone_name', 'phone_price')

class HeadphonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headphones
        fields = ('headphones_name', 'headphones_price')       