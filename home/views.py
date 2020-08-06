from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product

def index(request):
    """A view that displays the index page"""
    products = Product.objects.all()
    return render(request, "index.html", { 'products': products })

def payment_and_shipping(request):
    """
    Sends to a payment_and_shipping page for information purposes only.
    """
    return render(request, 'payment_and_shipping.html')

def returns_and_warranty(request):
    """
    Sends to a Returns and Warranty page for information purposes only.
    """
    return render(request, 'returns_and_warranty.html')