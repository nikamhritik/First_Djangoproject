from django.shortcuts import render, redirect
# from django.http import request
from .models import Product
# Create your views here.



def get_all_products(request):
    all_prod = Product.objects.all( )
    return render(request=request, template_name="products.html", context={"prods" : all_prod})

def create_products(request):
    if request.method == "POST":
        prd_name = request.POST.get("pm")
        prd_brand = request.POST.get("bm")
        prd_price = request.POST.get("prc")
        prd_quantity = request.POST.get("qn")
        
        if not request.POST.get("id"):
            Product.objects.create(name= prd_name, brand=prd_brand, price=prd_price, quantity = prd_quantity )
        else:
            prd = Product.objects.get(id=request.POST.get("id"))
            prd.name = prd_name,
            prd.brand = prd_brand,
            prd.price = prd_price,
            prd.quantity = prd_quantity
            prd.save()    
        return redirect("get_prods")
    elif request.method == "GET":        
        return render(request, "create_products.html")

def get_product(request, pid):
    prod = Product.objects.get(id = pid)
    return render(request, "create_products.html", {"single_product":prod})

def update_product(request, pid):
    pass

def delete_product(request, pid):
    Product.objects.delete(id = pid)
    return redirect("get_prods")