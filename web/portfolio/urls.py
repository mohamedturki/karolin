from django.conf.urls import url

from .views import (RecentProjectList,
                    CategoryDetail, project_detail, AboutBaseView)

urlpatterns = [
    url(r'^$', RecentProjectList.as_view(), name="recent"),
    url(r'^project/(?P<slug>[-\w]+)/$',
        CategoryDetail.as_view(
                template_name='portfolio/layouts/category_detail.html'
            ),
        name="category-detail"
        ),
    url(r'^project/(?P<category_slug>[-\w]+)/(?P<project_slug>\w+)/$',
        project_detail,
        name='project-detail'
        ),
    url(r'^about/$',
        AboutBaseView.as_view(template_name='portfolio/layouts/about.html'),
        name='about'
        ),
    url(r'^resume/$',
        AboutBaseView.as_view(template_name='portfolio/layouts/resume.html'),
        name='resume'
        ),
    url(r'^contact/$',
        AboutBaseView.as_view(template_name='portfolio/layouts/contact.html'),
        name='contact'
        ),
    url(r'^recommendation/$',
        AboutBaseView.as_view(
            template_name='portfolio/layouts/recommendation.html'
        ),
        name='recommendation'
        ),

]
