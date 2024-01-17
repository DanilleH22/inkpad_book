from django.contrib import admin
from .models import CreateBook, Categories, CreateChapter

# Register your models here.
admin.site.register(CreateBook)
admin.site.register(Categories)
admin.site.register(CreateChapter)
