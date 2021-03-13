from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'chetty/index.html')

def about(request):
    return render(request, 'chetty/about.html')

def shop(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'chetty/shop.html', context)

def shopdetails(request):
    return render(request, 'chetty/shopdetails.html')

def cart(request):
	return render(request, 'chetty/cart.html')

def checkout(request):
	return render(request, 'chetty/checkout.html')
	
def contact(request):
    return render(request, 'chetty/contact.html')