from . import views
from django.urls import path
from .views import BookList, BookChaptersView, BookmarkView, flipbook


urlpatterns = [
    path('', BookList.as_view(), name='browse'),
    path('<slug:slug>/', views.book_post, name='book_view'),
    path('<slug:book_slug>/chapters', BookChaptersView.as_view(), name='view_book_chapters'), 
    path('<slug:slug>/bookmark/', BookmarkView, name='bookmark_book'),
    path('<slug:slug>/reading', flipbook, name='read_book')
]
