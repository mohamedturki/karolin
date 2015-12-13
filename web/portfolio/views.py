import logging

from django.views.generic import ListView, DetailView

from .models import Project, ProjectCategory

logger = logging.getLogger(__name__)


class ProjectList(ListView):
    model = Project
    template_name = 'portfolio/layouts/index.html'
    context_object_name = 'projects'


class RecentProjectList(ProjectList):
    queryset = Project.objects.order_by('pub_date')[:4]


class ProjectDetail(DetailView):
    model = Project
    template_name = 'portfolio/layouts/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        context['similar_projects'] = Project.objects.filter(
            category=self.object.category
        ).exclude(slug=self.object.slug)[:3]

        return context
