from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import BookForm, ChapterForm
from .models import CreateBook, CreateChapter
from django.forms import forms


# Create your views here.
class BookCreation(LoginRequiredMixin, CreateView):
    template_name = 'book/book_outline.html'
    model = CreateBook
    form_class = BookForm
    success_url = reverse_lazy('book_chapter')

    def form_valid(self, form):
        if 'save_draft' in self.request.POST:
            # Handle save draft logic
            form.instance.status = 'Draft'
            form.save()
            return self.render_to_response(self.get_context_data(form=form))
        elif 'next' in self.request.POST:
            # Handle publish (or other logic) when 'Next' is clicked
            form.instance.status = 'Published'
            form.save()
            return redirect('book_chapter')
        else:
            return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        # Custom logic when the form is invalid (this method is called by CreateView)
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

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
        return redirect('completed_book')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def form_invalid(self, form):
        # If form is invalid
        return super().form_invalid(form)


class CompletedBook(LoginRequiredMixin, DetailView):
    template_name = 'book/completed_book.html'
    model = CreateBook
    slug = 'slug'
    context_object_name = 'book'
