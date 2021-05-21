from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ Displaying all products """

    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products, 
        'current_categories': categories,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Displaying product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add product """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully added!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Check your form input and try again.')
    else: 
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
