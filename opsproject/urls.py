"""opsproject URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from dbaproject import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^dbaproject/index.html/$',views.index),
    url(r'^dbaproject/messages.html/$',views.messages),
    url(r'^dbaproject/tasks.html/$',views.tasks),
    url(r'^dbaproject/ui.html/$',views.ui),
    url(r'^dbaproject/widgets.html/$',views.widgets),
    url(r'^dbaproject/submenu.html/$',views.submenu),
    url(r'^dbaproject/submenu2.html/$',views.submenu2),
    url(r'^dbaproject/submenu3.html/$',views.submenu3),
    url(r'^dbaproject/form.html/$',views.form),
    url(r'^dbaproject/chart.html/$',views.chart),
    url(r'^dbaproject/typography.html/$',views.typography),
    url(r'^dbaproject/gallery.html/$',views.gallery),
    url(r'^dbaproject/table.html/$',views.table),
    url(r'^dbaproject/calendar.html/$',views.calendar),
    url(r'^dbaproject/file-manager.html/$',views.filemanager),
    url(r'^dbaproject/icon.html/$',views.icon),
    url(r'^dbaproject/login.html/$',views.login),
    url(r'^dbaproject/inception.html/$',views.inception),
]
