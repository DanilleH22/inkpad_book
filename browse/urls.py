from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BookList


urlpatterns = [
    path('', BookList.as_view(), name='browse'),
    path('<slug:slug>/', views.book_post, name='book_view'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)