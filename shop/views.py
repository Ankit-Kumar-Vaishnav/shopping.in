from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    categorys = Product.objects.values('category','id')
    categorys = {item['category'] for item in categorys}
    allProds = []
    for category in categorys:
        products = Product.objects.filter(category=category)
        n = len(products)
        nSlids = n//4+ ceil((n/4)-(n//4))
        allProds.append([products,range(1,len(products)),range(1,nSlids),category])
    
    
    params = {
        'allProds' : allProds,
    }
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productview(request):
    return render(request, 'shop/productview.html')

def checkout(request):
    return render(request, 'shop/checkout.html')
