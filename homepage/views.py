from django.shortcuts import render
from .models import FunFact, Quotes

# Create your views here.


def home(request):
    # Retrieve three random fun facts from the database
    fun_facts = FunFact.objects.order_by('?')[:3]

    # Retrieve two random quotes from the database
    quotations = Quotes.objects.order_by('?')[2]

    return render(request, 'home.html', {'fun_facts': fun_facts})
