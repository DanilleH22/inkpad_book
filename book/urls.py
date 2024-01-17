from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BookCreation, BookChapter, CompletedBook

urlpatterns = [
    path('book_details/', BookCreation.as_view(), name='book_details'),
    path('book_chapter/', BookChapter.as_view(), name='book_chapter'),
    # path('completed_book/<slug:slug>',
    #      CompletedBook.as_view(),
    #      name='completed_book/'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
