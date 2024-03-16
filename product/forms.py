from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import *

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']