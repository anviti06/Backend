from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
import json

from .constant import Page
from .response import (
    response_login_intro,  response_login_options, 
    response_login_with_num , response_login_otp_verify, 
    response_login_otp_error, response_login_location
)        

@api_view(['POST', 'GET'])
def loginView(request):
    if request.method == 'GET':
        response = {
            Page.pg1.value : response_login_intro(Page.pg1.value),
            Page.pg2.value : response_login_intro(Page.pg2.value),
            Page.pg3.value : response_login_intro(Page.pg3.value),
        }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")


@api_view(['POST', 'GET'])
def loginOptionsView(request):
    if request.method == 'GET':
        response = {
            Page.pg4.value : response_login_options(Page.pg4.value),
        }        
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def loginNumberView(request):
    if request.method == 'GET':
        response = {
            Page.pg5.value : response_login_with_num(Page.pg5.value),
          }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")


@api_view(['POST', 'GET'])
def loginOtpVerify(request):
    if request.method == 'GET':
        response = {
            Page.pg6.value : response_login_otp_verify(Page.pg6.value),
        }
        
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def loginOtpError(request):
    if request.method == 'GET':
        response = {
            Page.pg7.value : response_login_otp_error(Page.pg7.value),
           }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")

@api_view(['POST', 'GET'])
def loginLocation(request):
    if request.method == 'GET':
        response = {
            Page.pg8.value : response_login_location(Page.pg8.value),
           }
        return HttpResponse(json.dumps(response), content_type = 'application/json')
    else:
        return HttpResponse("false")
