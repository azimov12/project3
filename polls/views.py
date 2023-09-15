from django.shortcuts import render, get_object_or_404
from .models import Phones, Headphones
from .serializers import PhonesSerializer, HeadphonesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

# Create your views here.

class Detail(generics.RetrieveAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer 

class All(generics.ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer 

class Detail2(generics.RetrieveAPIView):
    queryset = Headphones.objects.all()
    serializer_class = HeadphonesSerializer

class All2(APIView):
    queryset = Headphones.objects.all()
    serializer_class = HeadphonesSerializer  

class CreatePhoneView(generics.CreateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer  

class CreateHeadphoneView(generics.CreateAPIView):
    queryset = Headphones.objects.all()
    serializer_class = HeadphonesSerializer 

class DeletePhone(generics.DestroyAPIView):   
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer    

class DeleteHeadphone(generics.DestroyAPIView):   
    queryset = Headphones.objects.all()
    serializer_class = HeadphonesSerializer    

class UpdatePhone(generics.UpdateAPIView):   
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer    

class UpdateHeadphone(generics.UpdateAPIView):   
    queryset = Headphones.objects.all()
    serializer_class = HeadphonesSerializer     