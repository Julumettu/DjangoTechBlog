from django.contrib import admin

from .models import StandardTextPost,Comment

# Register your models here.
admin.site.register(StandardTextPost)
admin.site.register(Comment)
