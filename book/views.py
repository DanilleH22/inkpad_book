from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views.generic import View, DetailView, ListView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .forms import CreateBookForm, CreateChapterForm
from .models import CreateBook, CreateChapter
from django.forms import forms
from django.contrib import messages


# Create your views here.
class AddBook(LoginRequiredMixin, CreateView):
    """
    User can create a book
    """
    template_name = 'book/book_details.html'
    model = CreateBook
    form_class = CreateBookForm
    
    
    def form_valid(self, form):
        """
        Check form is valid - all fields have been completed
        Checks if user has clicked published or save as draft
        Success message given after
        """
        form.instance.author = self.request.user
        book = form.save()

        if int(form.cleaned_data['status']) == 0:
            messages.success(self.request, 'Success! Book saved as draft.')
        elif int(form.cleaned_data['status']) == 1:
            messages.success(self.request, 'Book published successfully.')

        return redirect('add_chapter', book_slug=book.slug)



class AddBookChapter(LoginRequiredMixin, CreateView):
    """
    User can create a chapter
    """
    template_name = 'book/add_chapter.html'
    model = CreateChapter
    form_class = CreateChapterForm

    def form_valid(self, form):
        """
        Check form is valid - all fields have been completed
        Checks if user has clicked published or save as draft
        Success message given after
        """
        book_slug = self.kwargs['book_slug']
        book = get_object_or_404(CreateBook, slug=book_slug)
        form.instance.book = book

        # Save the form but don't commit yet
        chapter = form.save(commit=False)

        if int(form.cleaned_data['status']) == 0:
            messages.success(self.request, 'Success! Chapter saved as draft.')
        elif int(form.cleaned_data['status']) == 1:
            messages.success(self.request, 'New chapter published successfully.')

        # Save the chapter with the selected status
        chapter.save()

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('completed_book') 


class CompletedBook(LoginRequiredMixin, ListView):
    """
    Collects the Create book model data just created by user by id
    """
    def get(self, request, *args, **kwargs):
        books = CreateBook.objects.latest('id')

        return render(
            request,
            'book/completed_book.html',
            {
                'books': books,
               
            }
        )


class EditChapter(LoginRequiredMixin, UpdateView):
    """
    Allows users to edit chapter created
    """
    template_name = 'book/edit_chapter.html'
    model = CreateChapter
    form_class = CreateChapterForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        """
        If valid success message is returned
        """
        response = super().form_valid(form)
        messages.success(self.request, 'Chapter has been updated successfully.')
        return response

class EditBookDetails(LoginRequiredMixin, UpdateView):
    """
    Allows users to edit book created
    """
    template_name = 'book/edit_book.html'
    model = CreateBook
    form_class = CreateBookForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        If valid success message is returned
        """
        response = super().form_valid(form)
        messages.success(self.request, 'Book has been updated successfully.')
        return response




class DeleteChapter(LoginRequiredMixin, DeleteView):
    """
    Finds chapter and redirects user to delete page 
    to confirm deletion of chapter
    """
    template_name = 'book/delete_chapter.html'
    model = CreateChapter
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        """
        If chapter deleted a success message is returned
        """
        messages.success(request, 'Chapter has been deleted successfully.')
        return super(DeleteChapter, self).delete(request, *args, **kwargs)


class DeleteBook(LoginRequiredMixin, DeleteView):
    """
    Finds book and redirects user to delete page 
    to confirm deletion of chapter
    """
    template_name = 'book/delete_book.html'
    model = CreateBook
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        """
        If chapter deleted a success message is returned
        """
        messages.success(request, 'Book has been deleted successfully.')
        return super(DeleteBook, self).delete(request, *args, **kwargs)

