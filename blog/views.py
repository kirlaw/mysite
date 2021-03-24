from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.

# 显示贴子列表
def post_list(request):
    posts = Post.publish.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


# 显示贴子内容
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish_year=year,
                             publish_month=month,
                             publish_day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
