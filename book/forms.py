from django import forms
from .models import CreateBook, CreateChapter


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = CreateBook
        fields = ["title", "genre", 'status', 'excerpt',
                  'synopsis', 'image']
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "genre": forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CreateChapterForm(forms.ModelForm):

    class Meta:
        model = CreateChapter
        fields = ['chapter', 'content', 'status']
        widgets = {
            "chapter": forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        exclude = ['book']
