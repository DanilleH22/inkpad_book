from django.shortcuts import render, get_object_or_404
from book.models import CreateBook, CreateChapter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages

# Create your views here.

def view_profile(request):
    user_books = request.user.books.filter(author=request.user)
    return render(request, 'profiles/profile.html', {'user_books': user_books})
