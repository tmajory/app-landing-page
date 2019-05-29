from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    html = 'HELLO WORLD'
    return HttpResponse(html)
