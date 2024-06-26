from django import forms
from .models import Create_text_post

class TextForm(forms.ModelForm):
    class Meta:
        model = Create_text_post
        fields = ['post',]
