from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import StandardTextPost,Comment,PostWithUploads
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
import os

def index(request):
    post_list = StandardTextPost.objects.order_by('-pub_date')
    template = loader.get_template('posts/index.html')
    context = {
        'post_list': post_list,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    return HttpResponse("Tää on vähän tyhjä vielä")

def singular_post(request, title):
    try:
        post = StandardTextPost.objects.get(pk=title)
    except ObjectDoesNotExist:
        pass
    try:
        comments = Comment.objects.filter(post=post).order_by('pub_date')
    except ObjectDoesNotExist:
        pass
    template = loader.get_template('posts/single_full_post.html')
    context = {
        'post': post,
        'comments': comments,
    }
    return HttpResponse(template.render(context, request))

def submit_comment(request):
    comment = Comment(post=StandardTextPost.objects.get(pk=request.POST['title']),comment=request.POST['username'] + ': ' + request.POST['comment'], pub_date=timezone.now())
    comment.save()
    return HttpResponseRedirect('/posts/single/' + request.POST['title'] + '/')

def submit_blog_post(request, submit):
    return HttpResponse("jee!")

def test_upload(request):
    #path="/var/lib/techblog/posts/static/uploads"
    #img_list = os.listdir(path)
    description = PostWithUploads.objects.order_by('file')
    template = loader.get_template('gallery.html')
    context = {
        #'images': img_list,
        'descriptions': description,
    }
    return HttpResponse(template.render(context, request))

def upload_something(request):
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:
            uploaded_file = request.FILES['document']
            post = request.POST['description']
            new_upload = PostWithUploads(post=post,file=uploaded_file)
            new_upload.save()
        return HttpResponseRedirect('/posts/upload_file')
    return render(request, 'upload.html')
