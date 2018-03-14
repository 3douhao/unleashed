from django.urls.conf import path, re_path

from .views import tag_detail, tag_list, startup_list, startup_detail, TagCreate, StartupCreate, NewsLinkCreate, NewsLinkUpdate, TagUpdate, NewsLinkDelete, TagDelete, StartupDelete, StartupUpdate

urlpatterns = [
    re_path(r'^newslink/create/$', NewsLinkCreate.as_view(), name='organizer_newslink_create'),
    re_path(r'^newslink/delete/(?P<pk>\d+)/$', NewsLinkDelete.as_view(), name='organizer_newslink_delete'),
    re_path(r'^newslink/update/(?P<pk>\d+)/$', NewsLinkUpdate.as_view(), name= 'organizer_newslink_update'),
    re_path(r'^startup/$', startup_list, name='organizer_startup_list'),
    re_path(r'^startup/create/$', StartupCreate.as_view, name='organzer_startup_create'),
    re_path(r'^startup/(?P<slug>[\w\-]+)/update/$', StartupUpdate.as_view(), name='organizer_startup_update'),
    re_path(r'startup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'),
    re_path(r'^startup/(?P<slug>[\w\-]+)/delete/$', StartupDelete.as_view(), name='organizer_startup_delete'),
    re_path(r'^tag/$', tag_list, name='organizer_tag_list'),
    re_path(r'^tag/create/$', TagCreate.as_view(), name='organizer_tag_create'),
    re_path(r'^tag/(?P<slug>[\w\-]+)/update/$', TagUpdate.as_view(), name='organizer_tag_update'),
    re_path(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
    re_path(r'^tag/(?P<slug>[\w-]+)/delete/$', TagDelete.as_view(), name='organizer_tag_delete'),
]
