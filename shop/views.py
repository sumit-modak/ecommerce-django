from django.shortcuts import render, HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    # products = Product.objects.all()
    # nSlides = ceil(len(products)/4)
    # # params = {"nSlides": nSlides, "range": range(1, nSlides), "products": products}
    # allProducts = [[products, range(1, nSlides), nSlides], 
    #                [products, range(1, nSlides), nSlides]]

    allProducts = []
    catProducts = Product.objects.values("category", "id")
    cats = {item['category'] for item in catProducts}
    for cat in cats:
        product = Product.objects.filter(category=cat)
        nSlides = ceil(len(product))
        allProducts.append([product, range(1, nSlides), nSlides])
        
    return render(request, "shop/index.html", {"allProducts": allProducts})

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
