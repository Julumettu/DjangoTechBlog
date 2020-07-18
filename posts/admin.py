from django.contrib import admin

from .models import StandardTextPost,Comment, PostWithUploads

# Register your models here.
admin.site.register(StandardTextPost)
admin.site.register(Comment)
admin.site.register(PostWithUploads)
