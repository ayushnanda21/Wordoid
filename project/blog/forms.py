from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("author","title","text")

    #to make edit/connect to particular form option to css class
    widgets={
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
    }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("author","text")

    #to make edit/connect to particular form option to css class
    widgets={
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
    }
