from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm, UserUpdateForm
from .models import Profile
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)
    
def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
        
    args = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'register.html', args)
    
@login_required
def update(request):
    """
    Update the profile of the logged in user
    """ 
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if hasattr(request.user, "profile"):
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
        else:
            profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            if not hasattr(request.user, "profile"):
                profile_form = profile_form.save(commit=False)
                profile_form.user = request.user
                profile_form.save()
            else:
                profile_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect(reverse('index'))
    else:
        user_form = UserUpdateForm(instance=request.user)
        if hasattr(request.user, "profile"):
            profile_form = ProfileForm(instance=request.user.profile)
        else:
            profile_form = ProfileForm()

    args = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'update.html', args)
    
