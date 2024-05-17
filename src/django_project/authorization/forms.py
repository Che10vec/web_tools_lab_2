from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import SafeString

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='sub-section'>"))

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='sub-section'>"))