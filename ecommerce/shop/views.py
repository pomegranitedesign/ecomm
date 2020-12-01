from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product


def index(request):
    product_name = request.GET.get('product_name')
    products = Product.objects.all()

    if product_name != '' and product_name is not None:
        products = Product.objects.filter(title__icontains=product_name)

    paginator = Paginator(products, per_page=4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'shop/index.html', {'products': products})


def details(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'shop/details.html', {'product': product})
