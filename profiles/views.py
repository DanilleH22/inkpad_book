from django.shortcuts import render, get_object_or_404
from book.models import CreateBook, CreateChapter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def view_profile(request):
    user_books = request.user.books.filter(author=request.user).exclude(status=0)
    drafts = request.user.books.filter(author=request.user).exclude(status=1)
    return render(
        request, 
        'profiles/profile.html', {
            'user_books': user_books,
            'drafts': drafts,
            }
            )


def book_draft(request, slug):
    view_drafts = get_object_or_404(CreateBook, slug=slug, status=0)
    return render(request, 'profiles/draft.html', {'view_drafts': view_drafts})


@login_required
def view_bookmark(request):
    bookmarked_books = request.user.bookmarked_books.all()

    return render(request, "profiles/bookmarked.html", {'bookmarked_books': bookmarked_books})
