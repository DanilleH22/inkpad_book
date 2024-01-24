from django.shortcuts import render, get_object_or_404
from .models import Bookmark
from django.urls import reverse_lazy, reverse
from book.models import CreateBook
from django.http import HttpResponseRedirect
# Create your views here.

@login_required
def bookmark_book(request, slug):
    # Get the book using its slug
    book = get_object_or_404(CreateBook, slug=request.POST.get('book_slug'))
    # 
    bookmark, created = Bookmark.objects.get_or_create(
        user=request.user,
        book=book
    )
    # book.bookmark.add(request.user)
    return HttpResponseRedirect(reverse('browse', args=[str(slug)]))