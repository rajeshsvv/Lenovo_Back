from django.shortcuts import render
from django.http import HttpResponse                # HttpResponse is class to create a response send to client
from .models import Product
# Create your views here.

def index(request):
    products=Product.objects.all()
    # return HttpResponse('Hello World')
    return render(request,'index.html',{'products':products})

def new(reuqest):
    return HttpResponse("New Products")