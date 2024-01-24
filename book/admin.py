from django.contrib import admin
from .models import CreateBook, Categories, CreateChapter
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Categories)


@admin.register(CreateBook)
class CreateBookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'synopsis', 'excerpt', )
    search_fields = ['title']
    list_filter = ('genre',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('synopsis', 'excerpt')


@admin.register(CreateChapter)
class CreateChapterAdmin(SummernoteModelAdmin):

    list_display = ('chapter', 'content', 'status')
    search_fields = ['chapter']
    list_filter = ('chapter',)
    summernote_fields = ('content',)
