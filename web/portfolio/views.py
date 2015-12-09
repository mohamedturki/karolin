import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

from .models import Project, ProjectCategory

logger = logging.getLogger(__name__)


def index(request):
    categories = ProjectCategory.objects.all()
    projects = Project.objects.filter()[:3]
    return render(request, 'portfolio/layouts/index.html', {
        'categories': categories,
        'projects': projects
    })


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/project.html', {'project': project})


def category(request, category_id):
    project_category = get_object_or_404(ProjectCategory, pk=category_id)
    projects = Project.objects.filter(category=project_category)
    return render(
        request,
        'portfolio/category.html',
        {
            'category': project_category,
            'projects': projects
        }
    )


def resume(request):
    return render(request, 'portfolio/resume.html')


# TODO: Refactor this to a class based view.
def about(request):
    if request.method == "POST":
        logger.info("post")
        try:
            name = request.POST['name']
            message = request.POST['message']
            logger.info('{0} sent you {1}'.format(name, message))
            return HttpResponseRedirect(reverse('portfolio:about'))
        except KeyError as e:
            logger.error("Error while sending a message. Error: {0}".format(e))
            return render(request, 'portfolio/about.html', {
                "error_message": "Oops"
            })
    else:
        return render(request, 'portfolio/about.html')
