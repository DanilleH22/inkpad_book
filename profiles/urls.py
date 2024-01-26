from . import views
from django.urls import path
from .views import view_profile, view_bookmark, book_draft


urlpatterns = [
    path('', view_profile, name='profile'),
    path('bookmarked/', view_bookmark, name='bookmarked'),
    path('<slug:slug>/draft/', book_draft, name='draft'),
    
]