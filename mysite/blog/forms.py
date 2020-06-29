from .models import Comment, Feedback
from django.template.defaultfilters import slugify
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'message')