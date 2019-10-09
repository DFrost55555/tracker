from django.contrib import admin
from .models import Project, ProjectResources

class ProjectResourcesAdmin(admin.ModelAdmin):
    list_display = ('pr_id', 'pr_project_fk', 'pr_customer_fk', 'pr_resource_fk')
    list_display_links = ('pr_id')
    list_per_page = 20

admin.site.register(Project)
admin.site.register(ProjectResources, ProjectResourcesAdmin)