from django.contrib import admin
from .models import FunFact, BookQuote
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(FunFact)
class FunFactAdmin(admin.ModelAdmin):
    list_display = ['fact',]
    search_fields = ['fact']
    summernote_fields = ('fact',)


@admin.register(BookQuote)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ['quote',]
    search_fields = ['quote']
    summernote_fields = ('quote',)
