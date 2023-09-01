from django.shortcuts import render, get_object_or_404
from .models import Phones, Headphones
from django.http import JsonResponse
from .serializers import PhonesSerializer, HeadphonesSerializer

# Create your views here.

def detail(request, phone_id):
    phones = get_object_or_404(Phones, id = phone_id)
    phone_data = PhonesSerializer(phones)
    
    return JsonResponse(phone_data.data, safe=False)

def all(request):
    phone = Phones.objects.all()
    res = PhonesSerializer(phone, many=True)
    
    return JsonResponse(res.data, safe=False)   


def detail2(request, headphone_id):
    headphone = get_object_or_404(Headphones, id = headphone_id)
    headphone_data = HeadphonesSerializer(headphone)
    
    return JsonResponse(headphone_data.data, safe=False)

def all2(request):
    headphone = Headphones.objects.all()
    result = HeadphonesSerializer(headphone, many=True)
    
    return JsonResponse(result.data, safe=False)      