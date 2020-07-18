from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('single/<str:title>/', views.singular_post, name='post'),
    path('submit_comment/', views.submit_comment, name='submit_comment'),
    path('upload_file', views.upload_something, name='upload_file'),
    path('uploaded_files',views.test_upload, name='file_upload'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
