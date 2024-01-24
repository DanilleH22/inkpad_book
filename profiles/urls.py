from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import view_profile, view_bookmark


urlpatterns = [
    path('', view_profile, name='profile'),
    path('bookmarked/', view_bookmark, name='bookmarked')
    
]