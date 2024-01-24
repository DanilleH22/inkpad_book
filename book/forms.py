from django import forms
from .models import CreateBook, CreateChapter


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = CreateBook
        fields = ["title", "genre", 'status', 'excerpt',
                  'synopsis', 'image']


class CreateChapterForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=CreateBook.objects.all(), required=True)

    class Meta:
        model = CreateChapter
        fields = ['chapter', 'content', 'status']
