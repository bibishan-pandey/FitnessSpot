from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from auths.forms import UserCreationForm
from auths.models import Profile


def register(request, *args, **kwargs):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('core:fitness-feed')

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()

        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        messages.success(request, f"Account for {username} created successfully.")

        # Authenticate the user and log them in
        user = authenticate(request, email=email, password=password)
        login(request, user)
        messages.success(request, f"Hi {username}, you are now logged in.")

        # Check if a profile already exists for this user
        profile, created = Profile.objects.get_or_create(user=user)
        if created:
            profile.phone = form.cleaned_data.get('phone')
            profile.gender = form.cleaned_data.get('gender')
            profile.save()
        else:
            messages.warning(request, f"A profile already exists for {username}.")

        return redirect('core:fitness-feed')

    context = {
        'form': form
    }
    return render(request, 'auths/register.html', context)


def signin(request, *args, **kwargs):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('core:fitness-feed')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Hi {user.username}, you are now logged in.")
            return redirect('core:fitness-feed')
        else:
            messages.error(request, "Invalid email or password. Please try again.")

    return render(request, 'auths/register.html')


def signout(request):
    logout(request)
    return redirect("auths:fitness-register")
