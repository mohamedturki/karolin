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
