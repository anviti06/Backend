from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
import json

from .constant import Page
from .response import (
    response_advance_filter, response_filter, 
    response_subscribe_elite
)        

@api_view(['POST', 'GET'])
def advanceFilter(request):
    if request.method == 'GET':
        response = {
            Page.pg1.value : response_advance_filter(Page.pg1.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")


@api_view(['POST', 'GET'])
def Filter(request):
    if request.method == 'GET':
        response = {
            Page.pg2.value : response_filter(Page.pg2.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")


@api_view(['POST', 'GET'])
def suscribeElite(request):
    if request.method == 'GET':
        response = {
            Page.pg3.value : response_subscribe_elite(Page.pg3.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")