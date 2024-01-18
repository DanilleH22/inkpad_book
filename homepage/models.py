from django.db import models

# Create your models here.


class FunFact(models.Model):
    fact = models.TextField(max_length=300, blank=False)

    def __str__(self):
        return self.fact


class BookQuote(models.Model):
    quote = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.quote
