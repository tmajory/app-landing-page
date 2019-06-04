from django.shortcuts import render

def dados(request):
    return render(request, 'dados/index.html')
