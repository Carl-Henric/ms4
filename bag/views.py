from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def view_bag(request):
    """ The view for rendering shopping bag """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Adding 1 of each product to shopping bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[item_id] = 1

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Removing item from shopping bag  """
    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)