from . import views
from django.urls import path
from .views import view_published, view_bookmark, book_draft


urlpatterns = [

    path('bookmarked/', view_bookmark, name='bookmarked'),
    path('draft/<slug:slug>/<int:pk>/', book_draft, name='draft'),
    path('published-books/', view_published, name='published-books'),
    
]