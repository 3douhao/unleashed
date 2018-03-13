"""suorganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls.conf import re_path, path, include

from organizer import urls as organizer_urls
from blog import urls as blog_urls
from .views import redirect_root

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', homepage),
    # re_path(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'), 
    re_path(r'^', include(organizer_urls)),
    re_path(r'^blog/', include(blog_urls)),
    re_path(r'^$', redirect_root),
]
