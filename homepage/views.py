from django.shortcuts import render
from .models import FunFact, BookQuote
from django.views import View

# Create your views here.


def home(request):
    # Retrieve three random fun facts from the database
    fun_facts = FunFact.objects.order_by('?')[:2]

    # Retrieve two random quotes from the database
    quotations = BookQuote.objects.order_by('?')[:2]

    return render(
        request,
        "homepage/index.html",
        {
            "fun_facts": fun_facts,
            "quotations": quotations,
        },
    )
