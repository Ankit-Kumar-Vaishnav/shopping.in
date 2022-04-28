from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
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
    name1 = request.POST.get('name','')
    email1 = request.POST.get('email','')
    phone1 = request.POST.get('phone','')
    query1 = request.POST.get('query','')
    d = Contact(name = name1,email= email1,phone=phone1,query=query1)
    d.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productview(request,id):
    # Fetch the product using the id
    product = Product.objects.filter(id=id)
    
    return render(request, 'shop/productview.html',{'product': product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')
