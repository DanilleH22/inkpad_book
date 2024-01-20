from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import BookForm, ChapterForm
from .models import CreateBook, CreateChapter
from django.forms import forms


# Create your views here.
class BookCreation(LoginRequiredMixin, CreateView):
    template_name = 'book/book_details.html'
    model = CreateBook
    form_class = BookForm
    success_url = reverse_lazy('book_chapter')

    def form_valid(self, form):
        form.save()
        return redirect('book_chapter')

    # def get_success_url(self):
    #     # Get the primary key of the newly created book
    #     book_id = self.object.id
    #     # Dynamically generate the URL for the book detail view
    #     success_url = reverse_lazy('book_detail', kwargs={'pk': book_id})
    #     return success_url


class BookChapter(LoginRequiredMixin, CreateView):
    template_name = 'book/book_chapter.html'
    model = CreateChapter
    form_class = ChapterForm
    success_url = reverse_lazy('completed_book')

    def form_valid(self, form):
        if 'save_draft' in self.request.POST:
            # Handle save draft logic
            form.instance.status = 'Draft'
        elif 'publish' in self.request.POST:
            # Handle publish (or other logic) when 'Publish' is clicked
            form.instance.status = 'Published'
        form.save()
        return redirect('completed_book')


class CompletedBook(LoginRequiredMixin, ListView):
    template_name = 'book/completed_book.html'
    model = CreateBook
    queryset = CreateBook.objects.filter()
    context_object_name = 'book_list'

    # def get(self, request, *args, **kwargs):
    #     title = kwargs.get('title')
    #     book = get_object_or_404(CreateBook, title=title)
    #     return render(request, self.template_name, {'book': book})