from django.shortcuts import get_object_or_404
from shipping.models import Shipping

def cart_shipping_regions(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    regions = Shipping.objects.all()
    selected_region = request.session.get('selected_region', regions[0])
    region_price = 0
    for region in regions:
        if region.name == selected_region:
            region_price = region.price
    
    return { 'regions': regions, 'selected_region': selected_region, 'region_price': region_price }
