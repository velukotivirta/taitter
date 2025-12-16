from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.

def posts_list(request):
    posts = Post.objects.all().order_by('-date') # Get all objects in Post
    return render(request, 'posts/posts_list.html', { 'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug) # Get object in Post where 'first-page' equals 'first-page'
    return render(request, 'posts/post_page.html', { 'post': post})

@login_required(login_url="/users/login/")

def post_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form })

@require_POST
@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if post.like_count == 0:
        post.like_count += 1
    else:
        post.like_count -= 1
    
    post.save()
    return JsonResponse({'like_count': post.like_count})