from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from .models import ProjectCategory, Project


class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopoulated_fields = {
        "slug": ("title",)
    }

admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Project, MarkdownModelAdmin)
