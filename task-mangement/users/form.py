from django import forms
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class CustomRegistrationsForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'confirm_password', 'email']

    # def clean_password1(self): # field error
    #     password1 = self.cleaned_data.get('password1')
    #     errors = []

    #     if len(password1) < 8:
    #         errors.append('Password must be at least 8 characters long.')
        
    #     if "abc" not in password1:
    #         errors.append("Password must include 'abc'.")

    #     if errors:
    #         raise forms.ValidationError(errors)

    #     return password1
    

    def clean(self):  # Non-field validation
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('confirm_password')

        errors = []

        # Check password length
        if password1 and len(password1) < 8:
            errors.append('Password must be at least 8 characters long.')

        # Check for "abc" in the password
        if password1 and "abc" not in password1:
            errors.append("Password must include 'abc'.")

        # Check if passwords match
        if password1 and confirm_password and password1 != confirm_password:
            errors.append('Passwords do not match.')

        # If there are any errors, raise them as non-field errors
        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data
    