from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(
                attrs={'type':"text", 'class':"form-control", 'id':"name", 'name':"name", 'placeholder':"Your Name", 'required data-error':"Please enter your name"}),
            'email': TextInput(
                attrs={'type': 'email', 'class': "form-control", 'id': "email", 'placeholder': "Your Email",
                       'required': "required", 'data-validation-required-message': "Please enter your email"}),
            'subject': TextInput(
                attrs={'type': "text", 'class': "form-control", 'id': "subject", 'placeholder': "Subject",
                       'required': "required", 'data-validation-required-message': "Please enter a subject"}),
            'message': Textarea(attrs={'class': "form-control", 'rows': "4", 'id': "message", 'placeholder': "Message",
                                       'required': "required",
                                       'data-validation-required-message': "Please enter your message"}),
        }