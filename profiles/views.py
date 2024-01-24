from django.shortcuts import render
from book.models import CreateBook, CreateChapter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def view_profile(request):
    user_books = request.user.books.filter(author=request.user)
    return render(request, 'profiles/profile.html', {'user_books': user_books})


@login_required
def view_bookmark(request):
    bookmarked_books = request.user.bookmarked_books.all()

    return render(request, "profiles/bookmarked.html", {'bookmarked_books': bookmarked_books})
