from django.conf.urls import url

from .views import RecentProjectList, ProjectDetail

urlpatterns = [
    url(r'^$', RecentProjectList.as_view()),
    url(r'^project/(?P<pk>\d+)/$',
        ProjectDetail.as_view(),
        name='project-detail'
        ),
]
