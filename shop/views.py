from django.shortcuts import render, HttpResponse
from .models import Product, Contact
from math import ceil

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

def cart(request):
    return render(request, "shop/cart.html")

def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, "shop/productView.html", {"product": product[0]})

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", 0)
        desc = request.POST.get("desc", "")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, "shop/contact.html")

def tracker(request):
    return render(request, ".html")

def search(request):
    return render(request, ".html")

def checkout(request):
    return render(request, ".html")
