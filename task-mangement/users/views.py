from django.shortcuts import render
from django.http import HttpResponse
from users.form import CustomRegistrationsForm

# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        form = CustomRegistrationsForm()

    if request.method == 'POST':
        form = CustomRegistrationsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration Successful!")
        else:
            print("Form is not valid")

    return render(request, 'registration/register.html', {'form': form})