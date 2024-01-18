from django.shortcuts import render, get_object_or_404
from book.models import CreateBook
from django.views import generic

# Create your views here.


class BookList(generic.ListView):
    queryset = CreateBook.objects.all()
    template_name = "browse/browse.html"
    paginate_by = 12


def book_post(request, slug):
    # queryset = CreateBook.objects.all()
    post = get_object_or_404(CreateBook, slug=slug)

    return render(
        request,
        "browse/book_view.html",
        {
            "book": post,
        },
    )
