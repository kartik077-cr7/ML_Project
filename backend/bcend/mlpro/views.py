from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def getPredictedText(request):
    data = json.loads(request.body)
    print("data is ",data['text'])

    return JsonResponse({'valid':1})