from django.urls import re_path
from . import views

app_name='comments'
urlpatterns = [
    re_path(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comments, name='post_comments'),
]