from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response (request handler or action)

def hello_word(request):
    return HttpResponse("Hello, World!")