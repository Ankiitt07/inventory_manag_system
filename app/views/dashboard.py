import json
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Count, Sum
from app.models import Product, RepairProduct, RejectedProduct, ProductTracking

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/home.html")
    else:
        return redirect('login')

def user_list(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, "dashboard/user_list.html", {'users' : users})
    else:
        return redirect('login')


def product_list(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        return render(request, "dashboard/product_list.html", {'products' : products})
    else:
        return redirect('login')


def repaired_product_list(request):
    if request.user.is_authenticated:
        repair_products = RepairProduct.objects.all()
        return render(request, "dashboard/repair_product_list.html", {'repair_products' : repair_products})
    else:
        return redirect('login')

def rejected_product_list(request):
    if request.user.is_authenticated:
        rejected_products = RejectedProduct.objects.all()
        return render(request, "dashboard/rejected_product_list.html", {'rejected_products' : rejected_products})
    else:
        return redirect('login')

def add_product(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            product_name = request.POST['name']
            product_quantity = request.POST['quantity']
            product_status = request.POST['status']

            if Product.objects.filter(product_name = product_name).exists():
                messages.error(request, 'Product already exist')
                return redirect('add_product')

            new_data_created = Product.objects.create(
                product_name = product_name,
                product_quantity = product_quantity,
                product_status = product_status
            )
            new_data_created.save()
            return redirect("product_list")
        else:
            return render(request, "dashboard/add_product.html")
    else:
        return redirect('login')

def add_product_in_assembly(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            product_id = request.POST['product']
            quantity = request.POST['quantity']
            status = int(request.POST['status'])
            event_date = timezone.now()

            new_data_created = ProductTracking.objects.create(
                product_id = product_id,
                quantity = quantity,
                event_date = str(event_date.date()),
                status = status
            )
            new_data_created.save()
            if status == 1:
                product_qty = Product.objects.get(product_id = product_id).product_quantity
                if int(quantity) > int(product_qty):
                    messages.error(request, 'Product shortage occur')
                    return redirect('add_product_in_assembly')
                else:
                    new_product_qty = int(product_qty) - int(quantity)
                    Product.objects.filter(product_id = product_id).update(product_quantity = new_product_qty)
                    return redirect("product_tracking")
            else:
                return redirect("product_tracking")
        else:
            products_data = Product.objects.filter(product_status = 1)
            return render(request, "dashboard/add_product_in_assembly.html", {'products_data': products_data})
    else:
        return redirect('login')


def update_product_in_assembly(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            product_id = request.POST['product_id']
            quantity = request.POST['product_quantity']
            status = int(request.POST['status'])
            event_date = timezone.now()

            new_data_created = ProductTracking.objects.create(
                product_id = product_id,
                quantity = quantity,
                event_date = str(event_date.date()),
                status = status
            )
            new_data_created.save()
            if status == 4:
                product_qty = Product.objects.get(product_id = product_id).product_quantity
                new_product_qty = int(product_qty) + int(quantity)
                Product.objects.filter(product_id = product_id).update(product_quantity = new_product_qty)
                return redirect("product_tracking")
            else:
                return redirect("product_tracking")
        else:
            products_data = ProductTracking.objects.get(pt_id = id)
            product_data = {
                "pt_id": products_data.pt_id,
                "product_id": products_data.product.product_id,
                "product_name": products_data.product.product_name,
                "quantity": products_data.quantity,
            }
            print(product_data)
            return render(request, "dashboard/update_product_in_assembly.html", {'products_data': product_data})
    else:
        return redirect('login')

def product_tracking(request):
    if request.user.is_authenticated:
        # products_in_assembly = ProductTracking.objects.values('product').distinct()
        products_in_assembly = ProductTracking.objects.all()
        return render(request, "dashboard/products_tracking.html", {'products_in_assembly' : products_in_assembly})
    else:
        return redirect('login')


def analytics_daily_production(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/analytics_daily_production.html")
    else:
        return redirect('login')

def analytics_monthly_production(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/analytics_monthly_production.html")
    else:
        return redirect('login')

def analytics_daily_packing(request):
    if request.user.is_authenticated:
        packed_products_count = ProductTracking.objects.filter(status= 1).values('event_date').annotate(total_quantity=Sum('quantity'))
        print(packed_products_count)
        return render(request, "dashboard/analytics_daily_packing.html",{'data': packed_products_count})
    else:
        return redirect('login')

def analytics_monthly_packing(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/analytics_monthly_packing.html")
    else:
        return redirect('login')

def analytics_daily_dispatch(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/analytics_daily_dispatch.html")
    else:
        return redirect('login')

def analytics_monthly_dispatch(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/analytics_monthly_dispatch.html")
    else:
        return redirect('login')

def analytics_daily_reject(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/analytics_daily_reject.html")
    else:
        return redirect('login')

def analytics_monthly_reject(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/analytics_monthly_reject.html")
    else:
        return redirect('login')