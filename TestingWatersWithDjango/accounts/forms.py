from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    #  Username rule: at least 6 characters
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username) < 6:
            raise forms.ValidationError("Username must be at least 6 characters long.")
       
        return username
    
     # Simplified password rule
    def clean_password1(self):
        password = self.cleaned_data.get("password1")

        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")

        if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
            raise forms.ValidationError("Password must contain both letters and numbers.")

        return password

