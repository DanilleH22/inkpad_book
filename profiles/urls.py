from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import view_profile


urlpatterns = [
    path('', view_profile, name='profile'),
]