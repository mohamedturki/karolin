from django.conf.urls import url

from .views import RecentProjectList

urlpatterns = [
    url(r'^$', RecentProjectList.as_view()),
]
