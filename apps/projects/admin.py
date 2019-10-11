from django.contrib import admin
from .models import Project, ProjectResources, ProjectItems, ProjectContact, ProjectNote

class ProjectResourcesAdmin(admin.ModelAdmin):
    list_display = ('pr_id', 'pr_project_fk', 'pr_customer_fk', 'pr_resource_fk')
    list_per_page = 20

admin.site.register(Project)
admin.site.register(ProjectResources, ProjectResourcesAdmin)
admin.site.register(ProjectItems)
admin.site.register(ProjectContact)
admin.site.register(ProjectNote)