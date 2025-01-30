from django.shortcuts import render, redirect
from users.forms import CustomRegistrationsForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from users.forms import LoginForm

# Create your views here.
def sign_up(request):
    form = CustomRegistrationsForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        print('user', user)
        user.set_password(form.cleaned_data.get('password1'))
        print(form.cleaned_data)
        user.is_active = False
        user.save()
        print(f"User {user.username} created and is active.")
        print(request.session)
        messages.success(request, "A Confirmation mail sent. Please check your email.")
        # form = CustomRegistrationsForm()
        return redirect('sign-in')
    elif request.method == 'POST' and not form.is_valid():
        print("Form is not valid:", form.errors)
        messages.error(request, "Please corect the errors below.")

    return render(request, 'registration/register.html', {'form': form})


def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
            
    return render(request, 'registration/login.html', {'form': form})


def sign_out(request):
    if request.method == 'POST':
        logout(request)
        # messages.success(request, "You have been logged out successfully.")
        return redirect('sign-in')
    