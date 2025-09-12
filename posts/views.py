# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def home_feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request , "home.html", {'posts': posts})


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')
    likes = post.likes.count()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'likes': likes
    })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'post_create.html', {'form': form})


