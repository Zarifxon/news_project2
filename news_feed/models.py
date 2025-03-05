from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)



class News(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"


    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')

    # news classi bilan category classini bog'laymiz'
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    upload_time = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=2,

                              choices=Status.choices,
                              default=Status.Draft)
    # PUBLISHED - NASHR QILINGANDAGI HOLAT
    # DRAFT - QORALAMA


# newsni published qilinganlarini chiqarish uchun

object = models.Manager()
published = PublishedManager()

class Meta:
    ordering = ['-publish_time'] #4 3 2 1 yangilik chiqishi ['publish_time'] 1 2 3 4

    def __str__(self):
        return self.title