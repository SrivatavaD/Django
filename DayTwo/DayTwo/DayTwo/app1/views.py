from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home Page')

def myfunction(request):
    return HttpResponse('Hello Django')

def learn_django(request, **kwargs):
    status = kwargs.get('Status', 'Not Allowed')
    return HttpResponse(f'<h1>Hello_Django - Status: {status}</h1>')



