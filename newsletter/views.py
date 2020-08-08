from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import NewsUserForm
from .models import NewsUser
from .emails import send_multiple_email

def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False) 
            if NewsUser.objects.filter(email=instance.email).exists():
                messages.error(request, f"{instance.email} is already subscribed to our mailing list.")
            else:
                instance.save()
                messages.success(request, "Successfully subscribed to our mailing list.")
                send_multiple_email(instance.email)
        else:
            messages.error(request, f"{form.data['email']} is not a valid email address.")
        return redirect(reverse('index'))
    else:
        form = NewsUserForm()
    
    return render(request, "subscribe.html", { 'form' : form })
    
"""
<form action="/newsletter/subscribe/" method="post">
	<input type="hidden" name="csrfmiddlewaretoken" value="VYQQ2witeZwsOth1ZJOfVQhJlNamEFjSeXbPQDqAY40Bl9sImrzrOdw2NvcjVjWT">
	<p><label for="id_email">Email:</label> <input type="email" name="email" maxlength="254" required="" id="id_email"></p>
	<button type="submit">Submit</button>
</form>
"""
