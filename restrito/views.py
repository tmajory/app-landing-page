from django.shortcuts import render
from django.http import HttpResponse

def restrito(request):
    return HttpResponse("Under Development")
    #return render(request, 'home/index.html')
