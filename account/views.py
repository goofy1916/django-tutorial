from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,'account/dashboard.html')

def products(request):
    return render(request,'account/products.html')

def contact(request):
    return HttpResponse('Contact us')

