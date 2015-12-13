import logging

from django.views.generic import ListView

from .models import Project, ProjectCategory

logger = logging.getLogger(__name__)


class ProjectList(ListView):
    model = Project
    template_name = 'portfolio/layouts/index.html'
    context_object_name = 'projects'


class RecentProjectList(ProjectList):

    def get_queryset(self, **kwargs):
        return Project.objects.order_by('pub_date')[:4]
