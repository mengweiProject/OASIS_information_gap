from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def get_num(request):
    a = int(request.GET.get('a'))
    b = int(request.GET.get('b'))

    return JsonResponse({'num': a + b})
