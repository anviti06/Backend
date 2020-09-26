from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
import json

from .constant import Page
from .response import (
    response_profile_basic, response_profile_advanced,
    response_manage_photos, response_select_source,
    response_about_you    
)        


@api_view(['POST', 'GET'])
def profileBasic(request):
    if request.method == 'GET':
        response = {
            Page.pg1.value : response_profile_basic(Page.pg1.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")


@api_view(['POST', 'GET'])
def profileAdvanced(request):
    if request.method == 'GET':
        response = {
            Page.pg2.value : response_profile_advanced(Page.pg2.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")


@api_view(['POST', 'GET'])
def managePhotos(request):
    if request.method == 'GET':
        response = {
            Page.pg3.value : response_manage_photos(Page.pg3.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")


@api_view(['POST', 'GET'])
def selectSource(request):
    if request.method == 'GET':
        response = {
            Page.pg4.value : response_select_source(Page.pg4.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")


@api_view(['POST', 'GET'])
def aboutYou(request):
    if request.method == 'GET':
        response = {
            Page.pg5.value : response_about_you(Page.pg5.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")
