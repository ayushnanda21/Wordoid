from django import forms
from blog.models import models

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
