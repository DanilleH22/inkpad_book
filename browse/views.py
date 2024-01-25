from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from book.models import CreateBook, CreateChapter
from django.views import generic
from django.views.generic import View, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Prefetch
# from book.forms import CreateChapterForm

# Create your views here.
@login_required
def BookmarkView(request, slug):
    if request.method == 'POST':
        book = get_object_or_404(CreateBook, slug=slug)
        bookmarked = False 
        if book.bookmark.filter(id=request.user.id).exists():
            book.bookmark.remove(request.user)
            bookmarked = False
        else:     
            book.bookmark.add(request.user)
            bookmarked = True 
         # Redirect to the referring page or a default page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/default-redirect/'))
    else:
        return redirect('home')


class BookList(generic.ListView):
    queryset = CreateBook.objects.filter(status=1)
    template_name = "browse/browse.html"
    paginate_by = 6
    context_object_name = 'book_list'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Get a list of book IDs that the user has bookmarked
            bookmarked_book_ids = self.request.user.bookmarked_books.values_list('id', flat=True)
            context['bookmarked_book_ids'] = bookmarked_book_ids
        return context


def book_post(request, slug):
    queryset = CreateBook.objects.filter()
    book_view = get_object_or_404(CreateBook, slug=slug)
        
    bookmarked = False
    if request.user.is_authenticated and book_view.bookmark.filter(id=request.user.id).exists():
        bookmarked = True
        

    context = {
        "book_view": book_view,
        "bookmarked": bookmarked,
        }

    return render(
        request,
        "browse/book_view.html", context
    )


class BookChaptersView(generic.ListView):
    model = CreateChapter
    template_name = 'browse/view_chapter.html'

    def get_queryset(self):
        book_slug = self.kwargs.get('book_slug')
        self.book = get_object_or_404(CreateBook, slug=book_slug)
        return CreateChapter.objects.filter(book=self.book)

    def get_context_data(self, **kwargs):
        # Include the book in the context
        context = super().get_context_data(**kwargs)
        context['book'] = self.book
        return context


def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        books = CreateBook.objects.all().filter(title__icontains=search)
        return render (request, 'searchbar.html', {
            "books": books
            }
            )



    # def form_valid(self, form):
    #     # Get book's slug from the URL
    #     book_slug = self.kwargs['book_slug']
    #     chapter_pk = self.kwargs['pk']
    #     # Retrieve the book
    #     book = get_object_or_404(CreateBook, slug=book_slug)
    #     chapter = get_object_or_404(CreateChapter, pk=chapter_pk)
    #     # Retrive the book chapter 

    #     return super().form_valid(form)
