from django.contrib import admin
from django.urls import include, path
from posts import views
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('user_management.urls')),
    path('posts/', include('posts.urls')),
    path('', views.index),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
]
