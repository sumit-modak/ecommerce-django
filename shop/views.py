from django.shortcuts import render, HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    nSlides = ceil(len(products)/4)
    params = {"nSlides": nSlides, "range": range(1, nSlides), "products": products}
    return render(request, "shop/index.html", params)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    return render(request, ".html")

def tracker(request):
    return render(request, ".html")

def search(request):
    return render(request, ".html")

def productView(request):
    return render(request, ".html")

def checkout(request):
    return render(request, ".html")
