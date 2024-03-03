from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    # views post_list
    posts = Post.published.all()  # all posts with status are retrieved PUBLISHED
    return render(request,
                  'blog/post/list.html',  # displaying the blog post list page
                  {'post': posts})  # passing the list of posts to the 'list.html' template


def post_detail(request, post_id):
    # views post_detail
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)  # we check status PUBLISHED If object not found, 404 error
    return render(request,
                  'blog/post/detail.html',  # # displaying the blog post list page
                  {'post': post})  # passing the list of posts to the 'detail.html' template
