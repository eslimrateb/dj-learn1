from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    ceratime = models.DateTimeField(default=timezone.now)
    draft = models.BooleanField(default=True)
    taggite = TaggableManager()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='post_user')
    image = models.ImageField(upload_to='posts')

    def __str__(self):
        return self.title
