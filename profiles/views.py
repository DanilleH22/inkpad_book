from django.shortcuts import render, get_object_or_404
from book.models import CreateBook, CreateChapter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def view_published(request):
    """
    Retrives all books linked ot the user, draft & published
    """
    published_books = request.user.books.filter(author=request.user).exclude(status=0) 
    return render(request, 'profiles/published-books.html', {
        'published_books': published_books,
        }
        )



def book_draft(request, slug, pk):
    """"
    Retrives all books linked to the user, draft. 
    """
    # Retrieve the draft book using slug and pk
    draft_book = get_object_or_404(CreateBook, slug=slug, pk=pk, status=0)
    
    # Retrieve the chapters related to the draft book
    draft_chapters = CreateChapter.objects.filter(book=draft_book, status=0)

     # Add the book's slug to each chapter for URL construction
    for chapter in draft_chapters:
        chapter.book_slug = draft_book.slug

    return render(request, 'profiles/draft.html', {
        'draft_book': draft_book,
        'draft_chapters': draft_chapters, 
    })



@login_required
def view_bookmark(request):
    """
    ALlow users to view books they have bookmarked
    """
    bookmarked_books = request.user.bookmarked_books.all()

    return render(request, "profiles/bookmarked.html", {'bookmarked_books': bookmarked_books})
