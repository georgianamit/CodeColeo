from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.content
