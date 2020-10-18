from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Title'
        }))
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter Content Here...',
            'cols': 100,
            'rows': 30
        }))
    # active = forms.BooleanField()
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]
