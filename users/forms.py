from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'placeholder': 'Your name', 'class': 'input-text', 'id': 'full-name'
        }
        self.fields['password1'].widget.attrs = {
            'placeholder': 'Your password', 'class': 'input-text', 'id': 'password'
        }
        self.fields['password2'].widget.attrs = {
            'placeholder': 'Confirm Password', 'class': 'input-text', 'id': 'confirm-password'
        }

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Your Email', 'class': 'input-text', 'id': 'your-email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your name', 'class': 'input-text', 'id': 'full-name'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password', 'class': 'input-text', 'id': 'password'
    }))
