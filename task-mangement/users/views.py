from django.shortcuts import render, redirect
from users.forms import CustomRegistrationsForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def sign_up(request):
    form = CustomRegistrationsForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        print('user', user)
        user.set_password(form.cleaned_data.get('password'))
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
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print("Doc", username, password)
        user = authenticate(request, username=username, password=password)
        # print(user)
        print(request.session)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Your account is inactive. Please contact admin.")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    
    return render(request, 'registration/login.html')


def sign_out(request):
    if request.method == 'POST':
        logout(request)
        # messages.success(request, "You have been logged out successfully.")
        return redirect('sign-in')
    