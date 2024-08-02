from django.shortcuts import render, HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json

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
        nSlides = ceil(len(product)/4)
        allProducts.append([product, range(1, nSlides), nSlides])
        
    return render(request, "shop/index.html", {"allProducts": allProducts})

def cart(request):
    return render(request, "shop/cart.html")

def productView(request, myid):
    print(request)
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

def checkout(request):
    if request.method == "POST":
        itemsJSON = request.POST.get("itemsJSON", "")
        name = request.POST.get("inputName", "")
        email = request.POST.get("inputEmail", "")
        phone = request.POST.get("inputPhone", "")
        address = request.POST.get("inputAddress", "")
        landmark = request.POST.get("inputLandmark", "")
        pincode = request.POST.get("inputPinCode", "")
        town_city = request.POST.get("inputTownCity", "")
        state = request.POST.get("inputState", "")
        country = request.POST.get("inputCountry", "")

        order = Order(items_json=itemsJSON, name=name, email=email, phone=phone,
                      address=address, landmark=landmark, pincode=pincode,
                      town_city=town_city, state=state, country=country)
        order.save()

        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        return render(request, "shop/checkout.html", {"thank": True, "id": order.order_id})
        
    return render(request, "shop/checkout.html")

def tracker(request):
    if request.method == "POST":
        orderID = request.POST.get("orderID", "")
        emailID = request.POST.get("emailID", "")
        try:
            order = Order.objects.filter(order_id=orderID, email=emailID)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderID)
                updates = []
                for item in updates:
                    updates.append({"desc": item.update_desc, "time": item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, "shop/tracker.html")

def search(request):
    return render(request, ".html")
