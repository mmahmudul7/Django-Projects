from django.shortcuts import render, redirect
from users.forms import CustomRegistrationsForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def sign_up(request):
    form = CustomRegistrationsForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Registration Successful!")
        form = CustomRegistrationsForm()
    elif request.method == 'POST' and not form.is_valid():
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
        if user is not None:
            login(request, user)
            return redirect('home')
    
    return render(request, 'registration/login.html')