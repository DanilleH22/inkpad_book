from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .forms import CreateBookForm, CreateChapterForm
from .models import CreateBook, CreateChapter
from django.forms import forms


# Create your views here.
class AddBook(LoginRequiredMixin, CreateView):
    template_name = 'book/book_details.html'
    model = CreateBook
    form_class = CreateBookForm
    
    def form_valid(self, form):
        # Set the author of the book
        form.instance.author = self.request.user
        # Save and get the created book instance
        self.object = form.save()
        # Redirect to add chapter with book's slug
        return redirect('add_chapter', book_slug=self.object.slug)


class AddBookChapter(LoginRequiredMixin, CreateView):
    template_name = 'book/add_chapter.html'
    model = CreateChapter
    form_class = CreateChapterForm

    def form_valid(self, form):
        # Get book's slug from the URL
        book_slug = self.kwargs['book_slug']
        # Retrieve the book
        book = get_object_or_404(CreateBook, slug=book_slug)
        # Associate the chapter with the book
        form.instance.book = book
        # Save the form
        return super().form_valid(form)
    
        
        # if 'save_draft' in self.request.POST:
        #     # Handle save draft logic
        #     form.instance.status = 0
        # elif 'publish' in self.request.POST:
        #     # Handle publish (or other logic) when 'Publish' is clicked
        #     form.instance.status = 1

    def get_success_url(self):
        return reverse('completed_book')


class CompletedBook(LoginRequiredMixin, ListView):
    template_name = 'book/completed_book.html'
    model = CreateBook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_book'] = CreateBook.objects.latest('pk')
        return context


class EditChapter(LoginRequiredMixin, UpdateView):
    template_name = 'book/edit_chapter.html'
    model = CreateChapter
    form_class = CreateChapterForm

    def get_success_url(self):
        return reverse('completed_book')
