from django.shortcuts import render, redirect, HttpResponse
import . from get_valid_IP_addresses
import json

def isValidIP(request, input):
    ipInQuestion = json.loads(input)
    if isinstance(ipInQuestion, str):
        return json.dumps(validIPAddresses(ipInQuestion))
