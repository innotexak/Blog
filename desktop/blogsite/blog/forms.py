from .models import Comment, Reply, Contact
from django.template.defaultfilters import slugify
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email','subject','body')

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('name', 'email','body')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email','subject','message')

