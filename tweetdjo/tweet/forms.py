from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
# Adjust to your model name

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']  # adjust field names
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'rows': 5,
                'placeholder': 'What’s on your mind?',
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control bg-dark text-light border-secondary',

            }),
        }


class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')