import datetime
from django.db import models
from django.template.defaultfilters import slugify
from django_markdown.models import MarkdownField


class ProjectCategory(models.Model):
    name = models.CharField(blank=False, max_length=100)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    class Meta:
        verbose_name_plural = 'Project categories'

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super(ProjectCategory, self).save()

    def get_absolute_url(self):
        return "/project/%s/" % self.slug


class Project(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    pub_date = models.DateTimeField(null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    thumbnail = models.ImageField(upload_to="thumbnails/", null=True)
    role = models.CharField(max_length=240, null=True)
    task = models.CharField(max_length=200, null=True)
    short_description = models.TextField(blank=True)
    full_description = MarkdownField()
    category = models.ForeignKey(ProjectCategory, null=True)

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Project, self).save()

    def get_absolute_url(self):
        return "/project/%s/%s" % (self.category.slug, self.slug)
