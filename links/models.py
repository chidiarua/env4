from django.db import models
from django.contrib.auth import get_user_model
from .managers import ActiveLinkManager


# Create your models here.


class Link(models.Model):
    description = models.CharField(max_length=200)
    target_url = models.URLField(max_length=200)
    objects = models.Manager()
    public = ActiveLinkManager()
    identifier = models.SlugField(
        max_length=20,
        blank=True,
        unique=True,
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.target_url
