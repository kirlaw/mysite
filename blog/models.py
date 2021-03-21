from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

# 博客贴子
class Port(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)  # 贴子标题
    slug = models.SlugField(max_length=250, unique_for_date='publish')  # 作简短标记（字母、下划线、数值、连字符)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)  # 创建时间
    updated = models.DateTimeField(auto_now=True)  # 贴子最后更新时间，每次更新时间自动保存
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Mate:
        ordering = ('-publish',)  # 降序排序，最新发布的贴子先显示

    def __str__(self):
        return self.title
