from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Categories(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name_plural = "categories"


class CreateBook(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True,
                            default='', blank=True)
    excerpt = models.TextField(max_length=200)
    biography = models.TextField(max_length=500, default='')
    image = models.ImageField(upload_to='images/')
    genre = models.ForeignKey(
        Categories, related_name='category', on_delete=models.SET_NULL,
        blank=True,
        null=True,)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CreateChapter(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    chapter = models.CharField(max_length=200)
    content = models.TextField()
    status = models.IntegerField(
        choices=((0, "Draft"), (1, "Published")), default=0)
