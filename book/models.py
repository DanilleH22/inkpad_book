from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField



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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', null=True, blank=True)
    status = models.IntegerField(
        choices=((0, "Draft"), (1, "Published")), default=0)
    excerpt = models.TextField(max_length=500)
    synopsis = models.TextField(max_length=1500, default='')
    image = CloudinaryField('image', default='placeholder')
    genre = models.ForeignKey(
        Categories, related_name='category', on_delete=models.SET_NULL,
        blank=True,
        null=True,)
    bookmark = models.ManyToManyField(User, related_name="bookmarked_books", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CreateChapter(models.Model):
    book = models.ForeignKey(CreateBook, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chapter', null=True, blank=True)
    chapter_id = models.AutoField(primary_key=True)
    chapter = models.CharField(max_length=200)
    content = models.TextField()
    status = models.IntegerField(
        choices=((0, "Draft"), (1, "Published")), default=0)
