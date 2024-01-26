from . import views
from django.urls import path
from .views import view_profile, view_bookmark, book_draft


urlpatterns = [
    path('', view_profile, name='profile'),
    path('bookmarked/', view_bookmark, name='bookmarked'),
    path('draft/<slug:slug>/<int:pk>/', book_draft, name='draft'),
    
]