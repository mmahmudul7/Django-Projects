from django import forms
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tasks.forms import StyledFormMixin
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class CustomRegistrationsForm(StyledFormMixin, forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'confirm_password', 'email']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise forms.ValidationError("This email is already registered. Please use a different email.")
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        # Regular expressions for password validation
        if not re.search(r'[A-Z]', password1):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password1):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'\d', password1):
            raise forms.ValidationError("Password must contain at least one digit.")
        if not re.search(r'[@$!%*?&]', password1):
            raise forms.ValidationError("Password must contain at least one special character (@, $, !, %, *, ?, &).")
        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        
        return password1

    def clean(self):  # Non-field validation
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('confirm_password')

        errors = []

        # Check if passwords match
        if password1 and confirm_password and password1 != confirm_password:
            errors.append('Passwords do not match.')

        # If there are any errors, raise them as non-field errors
        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data
    

class LoginForm(StyledFormMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)