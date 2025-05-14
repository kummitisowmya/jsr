from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']
class LoginForm(AuthenticationForm):  # ✅ CORRECT: inherits from AuthenticationForm
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))




