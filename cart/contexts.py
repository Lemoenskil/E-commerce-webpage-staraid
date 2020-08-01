from django.shortcuts import get_object_or_404
from products.models import Product
from shipping.models import Shipping


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    sub_total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        item_total = quantity * product.price
        sub_total += item_total
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product, 'total': item_total})

    regions = Shipping.objects.all()
    try:
        default_region = regions[0]
    except IndexError:
        default_region = ""
    selected_region = request.session.get('selected_region', default_region)
    region_price = 0
    for region in regions:
        if region.name == selected_region:
            region_price = region.price
    
    total = sub_total + region_price
    
    return {
        'product_count': product_count,
        'cart_items': cart_items,
        'sub_total': sub_total,
        'total': total,
        'regions': regions,
        'selected_region': selected_region,
        'region_price': region_price
    }

