from django import forms
from .models import CreateBook, CreateChapter


class BookForm(forms.ModelForm):
    class Meta:
        model = CreateBook
        fields = ["title", "genre", 'excerpt',
                  'biography', 'image']


class ChapterForm(forms.ModelForm):
    class Meta:
        model = CreateChapter
        fields = ['chapter_id', 'chapter', 'content', 'status']
