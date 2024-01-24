from . import views
from django.urls import path
from .views import AddBook, AddBookChapter, CompletedBook, DeleteChapter, EditChapter

urlpatterns = [
    path('book_details/', AddBook.as_view(), name='book_details'),
    path('<slug:book_slug>/add_chapter/', AddBookChapter.as_view(), name='add_chapter'),
    path('completed_book/',
         CompletedBook.as_view(),
         name='completed_book'),
    path('<slug:book_slug>/edit_chapter/<int:pk>/', EditChapter.as_view(), name='edit_book_chapter'),
    path('<slug:book_slug>/<int:pk>/delete', DeleteChapter.as_view(), name='delete_book_chapter'),
    
]


