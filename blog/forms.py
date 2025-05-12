from django import forms
from .models import Post


class Post_forms(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ('author',)
