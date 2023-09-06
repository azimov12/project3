from django.shortcuts import render, get_object_or_404
from .models import Phones, Headphones
from django.http import JsonResponse
from .serializers import PhonesSerializer, HeadphonesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class Detail(APIView):
    def get(self, request, *args, **kwargs):
        phone = get_object_or_404(Phones, id = kwargs['phone_id'])
        res = PhonesSerializer(phone)
        return Response(res.data)

class All(APIView):    
    def get(self, request):
        phone = Phones.objects.all()
        result = PhonesSerializer(phone, many=True)
        
        return Response(result.data)   


class Detail2(APIView):
    def get(self, request, *args, **kwargs):
        headphone = get_object_or_404(Headphones, id = kwargs['headphone_id'])
        result = HeadphonesSerializer(headphone)

        return Response(result.data)

class All2(APIView):
    def get(self, request):
        h = Headphones.objects.all()
        r = HeadphonesSerializer(h, many=True)

        return Response(r.data)   

class CreatePhoneView(APIView):
    def post(self, request):
        user_body = request.data 
        serializer = PhonesSerializer(data = user_body)          
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)    

class CreateKeyboardView(APIView):
    def post(self, request):
        user_body = request.data 
        s = HeadphonesSerializer(data = user_body)          
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors)    