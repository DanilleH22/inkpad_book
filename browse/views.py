from django.shortcuts import render, get_object_or_404
from book.models import CreateBook
from django.views import generic

# Create your views here.


class BookList(generic.ListView):
    queryset = CreateBook.objects.filter(status=1)
    template_name = "browse/browse.html"
    paginate_by = 6
    context_object_name = 'book_list'


def book_post(request, slug):
    queryset = CreateBook.objects.filter()
    book = get_object_or_404(CreateBook, slug=slug)

    return render(
        request,
        "browse/book_view.html",
        {
            "book": book,
        },
    )
