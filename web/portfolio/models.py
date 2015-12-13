import datetime
from django.db import models
from django_markdown.models import MarkdownField


class ProjectCategory(models.Model):
    name = models.CharField(blank=False, max_length=100)

    class Meta:
        verbose_name_plural = 'Project categories'

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    pub_date = models.DateField(auto_now_add=True, null=True)
    short_description = models.TextField(blank=True)
    full_description = MarkdownField()
    category = models.ForeignKey(ProjectCategory, null=True)

    def __str__(self):
        return self.title
