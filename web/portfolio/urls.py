from django.conf.urls import url

from .views import (index, category, project, resume, about)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^category/(?P<category_id>[0-9]+)/$', category, name="category"),
    url(r'^project/(?P<project_id>[0-9]+)/$', project, name="project"),
    url(r'^resume/$', resume, name="resume"),
    url(r'^about/$', about, name="about"),
]
