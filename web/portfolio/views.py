import logging

from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, render_to_response

from .models import Project, ProjectCategory

logger = logging.getLogger(__name__)


class ProjectList(ListView):
    model = Project
    template_name = 'portfolio/layouts/index.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()

        return context


class RecentProjectList(ProjectList):
    queryset = Project.objects.order_by('-pub_date')[:3]

    def get_context_data(self, **kwargs):
        context = super(RecentProjectList, self).get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()

        return context


class CategoryDetail(DetailView):
    model = ProjectCategory
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(
            category=self.object).order_by('-pub_date')
        context['categories'] = ProjectCategory.objects.all()

        return context


def project_detail(request, category_slug, project_slug):
    category = get_object_or_404(ProjectCategory, slug__iexact=category_slug)
    project = get_object_or_404(
        Project,
        slug__iexact=project_slug,
        category=category
    )
    similar_projects = Project.objects.filter(
        category=category
    ).exclude(slug=project_slug)[:3]
    categories = ProjectCategory.objects.all()

    return render_to_response(
        'portfolio/layouts/project_detail.html',
        {
            'category': category,
            'project': project,
            'similar_projects': similar_projects,
            'categories': categories
        }
    )


class AboutBaseView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(AboutBaseView, self).get_context_data(**kwargs)
        context['categories'] = [
            {
                'id': 'about',
                'name': 'About me'
            },
            {
                'id': 'resume',
                'name': 'Resumé'
            },
            {
                'id': 'testimonial',
                'name': 'Testimonial'
            },
            {
                'id': 'contact',
                'name': 'Contact me'
            },
        ]

        return context
