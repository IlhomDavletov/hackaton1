
from django import forms

from .models import *


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'



#comment

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'





