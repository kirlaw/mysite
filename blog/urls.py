#!/usr/bin/python3
# author eloise

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detial'),
    path('tag/<slug:tag_slug>', views.post_list, name='post_list_by_tag'),
]
