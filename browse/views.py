from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from book.models import CreateBook, CreateChapter
from django.views import generic
from django.views.generic import View, DetailView, ListView, UpdateView
from django.urls import reverse_lazy, reverse
# from book.forms import CreateChapterForm

# Create your views here.


class BookList(generic.ListView):
    queryset = CreateBook.objects.filter(status=1)
    template_name = "browse/browse.html"
    paginate_by = 6
    context_object_name = 'book_list'


def book_post(request, slug):
    queryset = CreateBook.objects.filter()
    book_view = get_object_or_404(CreateBook, slug=slug)

    return render(
        request,
        "browse/book_view.html",
        {
            "book_view": book_view,
        },
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


class EditChapter(LoginRequiredMixin, UpdateView):
    template_name = 'browse/edit_chapter.html'
    model = CreateChapter
    fields = ['chapter', 'content', 'status']

    def get_success_url(self):
        # Define where to redirect after successful update
        return reverse('completed_book')


    # def form_valid(self, form):
    #     # Get book's slug from the URL
    #     book_slug = self.kwargs['book_slug']
    #     chapter_pk = self.kwargs['pk']
    #     # Retrieve the book
    #     book = get_object_or_404(CreateBook, slug=book_slug)
    #     chapter = get_object_or_404(CreateChapter, pk=chapter_pk)
    #     # Retrive the book chapter 

    #     return super().form_valid(form)
