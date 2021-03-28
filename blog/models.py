from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.

# 管理器
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


# 博客贴子
class Post(models.Model):
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

    tags = TaggableManager()
    
    class Mate:
        ordering = ('-publish',)  # 降序排序，最新发布的贴子先显示

    def __str__(self):
        return self.title

    object = models.Manager()
    published = PublishedManager()

    # 链接到特定贴子
    def get_absolute_url(self):
        return reverse('blog:post_detial',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


# 评论系统
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
