from django.shortcuts import render, redirect, reverse
from shipping.models import Shipping

def adjust_region(request):
    """
    Adjust the shipping region in the shopping cart
    """
    print('adjust_region')
    regions = Shipping.objects.all()
    new_selected_region = request.POST.get('selected_region', [ regions[0] ])
    request.session['selected_region'] = new_selected_region

    return redirect(reverse('view_cart'))
