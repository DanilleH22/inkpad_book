from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookList.as_view(), name='browse'),
    path('<slug:slug>/', views.book_post, name='book_view'),
]
