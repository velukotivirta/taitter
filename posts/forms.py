from django import forms 
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'banner' ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write your post content here...'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Write your slug here...'}),
            'banner': forms.FileInput(attrs={'placeholder': 'Choose an image'}),
        }