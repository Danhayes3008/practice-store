from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.forms import LoginForm, RegistrationForm

# This def will show us the index.html page 
def index(request):
    return render(request, 'index.html')
    

# This def creates the login capability and uses the login form from the forms.py file
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, "Welcome to 24 hour online conveniance store!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect. Please try again")
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})


# this def is used to log the current user out from the site. It can only been done if the user is logged in
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Thank you for shopping at 24'hrs. Please come again")
    return redirect(reverse('index'))

# this registration def is used to allow new users to register for an account
def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Welcome to the 24 hour conveniance store")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = RegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})
        
def user_profile(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})