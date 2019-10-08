from django.contrib import admin
from .models import Resource, ResourceType


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('res_firstname', 'res_lastname', 'res_resource_type')
    list_per_page = 20
    ordering = ('res_lastname',)

admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceType)
