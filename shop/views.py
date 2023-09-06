from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Index Shop")
    return render(request, "shop/index.html")

def about(request):
    return render(request, ".html")

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