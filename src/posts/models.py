import re

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from hashtags.signals import parsed_hashtags
# Create your models here.

class PostManager(models.Manager):
    def share(self, user, parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj

        qs = self.get_queryset().filter(user=user, parent= og_parent).filter(timestamp__year=timezone.now().year,timestamp__month=timezone.now().month, timestamp__day=timezone.now().day)
        if qs.exists():
            return None

        obj = self.model(
            parent = og_parent,
            user = user,
            content = parent_obj.content
        )
        obj.save()
        return obj

class Post(models.Model):
    parent = models.ForeignKey("self",blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=155)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = PostManager()
    class Meta:
        ordering = ['-timestamp']
    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.content


def post_save_receiver(sender, instance, created, *args, **kwargs):
    if created and not instance.parent:
        user_regx = r'@(?P<username>[\w.@+-]+)'
        usernames = re.findall(user_regx, instance.content)

        hash_regx = r'#(?P<hashtag>[\w\d-]+)'
        hashtags = re.findall(hash_regx, instance.content)
        parsed_hashtags.send(sender=instance.__class__, hashtag_list = hashtags)


post_save.connect(post_save_receiver, sender=Post)