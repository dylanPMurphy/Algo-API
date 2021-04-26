from django.shortcuts import render, redirect, HttpResponse
from . import get_valid_IP_addresses
import json

def index(request):
    return HttpResponse("Success")
def isValidIP(request, input):
    return request

