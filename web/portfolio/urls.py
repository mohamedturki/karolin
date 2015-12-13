from django.conf.urls import url
from django.views.generic import TemplateView

from .views import RecentProjectList, ProjectDetail

urlpatterns = [
    url(r'^$', RecentProjectList.as_view(), name="recent"),
    url(r'^project/(?P<slug>\w+)/$',
        ProjectDetail.as_view(),
        name='project-detail'
        ),
    url(r'^about/$',
        TemplateView.as_view(template_name='portfolio/layouts/about.html'),
        name='about'
        ),
    url(r'^resume/$',
        TemplateView.as_view(template_name='portfolio/layouts/resume.html'),
        name='resume'
        ),
    url(r'^contact/$',
        TemplateView.as_view(template_name='portfolio/layouts/contact.html'),
        name='contact'
        ),
    url(r'^recommendation/$',
        TemplateView.as_view(
            template_name='portfolio/layouts/recommendation.html'
        ),
        name='recommendation'
        ),

]
