from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from .models import ProjectCategory, Project

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",)
    }
