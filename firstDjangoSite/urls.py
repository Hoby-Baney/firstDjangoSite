"""firstDjangoSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from firstApp.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello$', hello_world),
    url(r'^$', home),
    url(r'^index.html$', home),
    url(r'^about.html$', about),
    url(r'^services.html$', service),
    url(r'^contact.html$', contact),
    url(r'^portfolio-1-col.html$', por1),
    url(r'^portfolio-2-col.html$', por2),
    url(r'^portfolio-3-col.html$', por3),
    url(r'^portfolio-4-col.html$', por4),
    url(r'^portfolio-item.html$', porItem),
    url(r'^blog-home-1.html$', blog1),
    url(r'^blog-home-2.html$', blog2),
    url(r'^blog-post.html$', blogPost),
    url(r'^full-width.html$', fullWidth),
    url(r'^sidebar.html$', sidebar),
    url(r'^faq.html$', faq),
    url(r'^404.html$', pageNotFound),
    url(r'^pricing.html$', pricing),
    # 搜尋頁面
    url(r'^search$', search_view),
    #登入頁面
    url(r'^login$', login_view),
    #課程資訊
    url(r'^courseDetail$', courseDetail_view),


]
