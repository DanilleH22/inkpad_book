from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AddBook, AddBookChapter, CompletedBook, EditChapter

urlpatterns = [
    path('book_details/', AddBook.as_view(), name='book_details'),
    path('<slug:book_slug>/add_chapter/', AddBookChapter.as_view(), name='add_chapter'),
    path('completed_book/',
         CompletedBook.as_view(),
         name='completed_book'),
    path('<slug:book_slug>/edit_chapter/<int:pk>/', EditChapter.as_view(), name='edit_chapter'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
