from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from .models import ProjectCategory, Project

admin.site.register(ProjectCategory)
admin.site.register(Project, MarkdownModelAdmin)
