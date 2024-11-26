from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Product.objects.create(name=name, description=description, price=price)
        return redirect('product_list')
    return render(request, 'products/add_product.html')

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')