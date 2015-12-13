from django.conf.urls import url
from django.views.generic import TemplateView

from .views import RecentProjectList, ProjectDetail

urlpatterns = [
    url(r'^$', RecentProjectList.as_view()),
    url(r'^project/(?P<slug>\w+)/$',
        ProjectDetail.as_view(),
        name='project-detail'
        ),
]
