from django.shortcuts import render, redirect, reverse
from shipping.models import Shipping

def adjust_region(request):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    regions = Shipping.objects.all()
    new_selected_region = request.POST.get('selected_region', [ regions[0] ])
    request.session['selected_region'] = new_selected_region

    return redirect(reverse('view_cart'))
