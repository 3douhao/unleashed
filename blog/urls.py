from django.urls import re_path
from .views import PostList, post_detail, PostCreate, PostUpdate, PostDelete
urlpatterns = [
    re_path(r'^$', PostList.as_view(template_name='blog/post_list.html'), name='blog_post_list'),
    re_path(r'^create/$', PostCreate.as_view(), name='blog_post_create'),
    re_path(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w-]+)/'r'update/$', PostUpdate.as_view(), name='blog_post_update'),
    re_path(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$', post_detail, name='blog_post_detail'),
    re_path(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\=]+)/'r'delete/$', PostDelete.as_view(), name='blog_post_delete'),
]
