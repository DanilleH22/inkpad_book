from django.db import models

# Create your models here.


class FunFact(models.Model):
    fact = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.fact


class Quotes(models.Model):
    quote = models.TextField(max_length=300, blank=False)

    def __str__(self):
        return self.quote
