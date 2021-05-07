from django.shortcuts import render

# Create your views here.

def index(request):
    """ The view for returning index page """
    
    return render(request, 'home/index.html')