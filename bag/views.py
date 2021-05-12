from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ The view for rendering shopping bag """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Adding 1 of each product to shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    messages.success(request, f'{product.year}´s {product.brand} {product.name} added to your bag')

    bag[item_id] = 1

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Removing item from shopping bag  """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'{product.year}´s {product.brand} {product.name} Removed from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing watch: {e}')
        return HttpResponse(status=500)