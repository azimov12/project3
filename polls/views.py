from django.shortcuts import render, get_object_or_404
from .models import Phones, Headphones
from django.http import JsonResponse

# Create your views here.

def detail(request, phone_id):
    a = Phones.objects.get_object_or_404(id=phone_id)
    data = {
        'phone_name': a.phone_name,
        'phone_price': a.phone_price
    }
    return JsonResponse(data, safe=False)

def all(request):
    result = []
    all_data = Phones.objects.all()
    for ele in all_data:
        result.append({
            'phone_name': ele.phone_name,
            'phone_price': ele.phone_price
        })
    return JsonResponse(result, safe=False)   


def detail2(request, headphone_id):
    a = Headphones.objects.get_object_or_404(id=headphone_id)
    data = {
        'headphone_name': a.headphone_name,
        'headphone_price': a.headphone_price
    }
    return JsonResponse(data, safe=False)

def all2(request):
    result = []
    all_data = Headphones.objects.all()
    for ele in all_data:
        result.append({
            'headphone_name': ele.headphone_name,
            'headphone_price': ele.headphone_price
        })
    return JsonResponse(result, safe=False)       