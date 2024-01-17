from django.contrib import admin
from .models import FunFact, Quotes

# Register your models here.


@admin.register(FunFact)
class FunFactAdmin(admin.ModelAdmin):
    list_display = ['fact']


@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ['quote']
