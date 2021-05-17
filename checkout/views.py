from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty for the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
            'order_form': order_form,
            'stripe_public_key': 'pk_test_51Is1UfBkUAisrbi8KVV9r84VHRgu4QbVHiJIg9xXBSQ1TOzkqmtlzdk4zVYMeNPqMCJ4dUHuMAtmx4EE68DF7kPg00gPtQuYaR',
            'client_secret': 'test client secret',
        }

    return render(request, template, context)
