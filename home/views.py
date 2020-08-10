from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product
from home.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

def index(request):
    """A view that displays the index page"""
    products = Product.objects.all()
    return render(request, "index.html", { 'products': products })

def payment_and_shipping(request):
    """
    Sends to a payment_and_shipping page for information purposes only.
    """
    return render(request, 'payment_and_shipping.html')
    
def staraid(request):
    """
    Sends to a features page for information purposes only.
    """
    return render(request, 'staraid.html')

def returns_and_warranty(request):
    """
    Sends to a Returns and Warranty page for information purposes only.
    """
    return render(request, 'returns_and_warranty.html')

def terms_and_conditions(request):
    """
    Sends to a terms_and_conditions page for information purposes only.
    """
    return render(request, 'terms_and_conditions.html')
    
    privacy
    
def privacy(request):
    """
    Sends to privacy for information purposes only.
    """
    return render(request, 'privacy.html')
    
def cookies(request):
    """
    Sends to privacy for information purposes only.
    """
    return render(request, 'cookies.html')
    
def contact(request):
    form_class = ContactForm
    
    """
    Sends contact form.
    """
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['smith.goossens@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })