from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('single/<str:title>/', views.singular_post, name='post'),
    path('submit_comment/', views.submit_comment, name='submit_comment'),
]
