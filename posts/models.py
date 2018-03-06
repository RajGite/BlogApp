from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    category = models.CharField(max_length=128)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  reverse("posts:detail", kwargs={ "id":self.id})
        # "/posts/%s" %(self.id)
class UsersCategories(models.Model):
    user = models.CharField(max_length=128)
    category = models.CharField(max_length=128)

    class Meta:
        unique_together = ["user", "category"]
    def __unicode__(self):
        return self.user

    def __str__(self):
        return self.user