from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    # manager for working with published posts
    def get_queryset(self):
        # filters objects by status PUBLISHED
        return super().get_queryset()\
                      .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    # Post model

    class Status(models.TextChoices):
        # types of statuses
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)  # Post title
    slug = models.SlugField(max_length=250)  # Post slug
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')  # Post author
    body = models.TextField()  # Post body
    publish = models.DateTimeField(default=timezone.now)  # Post publish
    created = models.DateTimeField(auto_now_add=True)  # Post created
    update = models.DateTimeField(auto_now=True)  # Post update
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)  # Post status
    objects = models.Manager()  # default manager
    published = PublishedManager()  # application-specific manager

    class Meta:
        # Sorts results by publish returns in reverse chronological order
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
