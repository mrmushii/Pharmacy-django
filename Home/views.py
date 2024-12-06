from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Products


# Create your views here.


def index(request):
  return render(request, 'index.html')

def equipment(request):
    products = Products.objects.all()  # Fetch all products
    return render(request, 'equipment.html', {'products': products})
  
def product_page(request):
  return render(request, 'product_page.html')