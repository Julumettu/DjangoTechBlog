from django.db import models
from django.contrib import admin
import os
# Create your models here.

class StandardTextPost(models.Model):
    title = models.CharField(max_length=200)
    blog_text = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
    def short_text(self):
        return self.blog_text[:50] + "..."

class Comment(models.Model):
    post = models.ForeignKey('StandardTextPost', on_delete=models.CASCADE,)
    comment = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.comment

class PostWithUploads(models.Model):
    post = models.CharField(max_length=500)
    file = models.FileField()

    def filename(self):
        return os.path.basename(self.file.name)
