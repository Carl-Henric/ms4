from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ The view for rendering shopping bag """
    
    return render(request, 'bag/bag.html')
