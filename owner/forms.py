from django import forms
from django.contrib.auth.models import User
from Api.models import Product
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password"]
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"