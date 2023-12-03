from django import forms

from . import models



class image_form(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ['image', 'caption']

class post_form(forms.ModelForm):
    edit_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Post
        fields = ['title', 'content']

class delete_post_form(forms.Form):
    delete_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)