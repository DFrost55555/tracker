from django.contrib import admin
from .models import ServiceArea

class SvcAreaAdmin(admin.ModelAdmin):
    list_display = ('svcarea_name', 'svcarea_createdby', 'svcarea_createddate', 'svcarea_modifiedby', 'svcarea_modifieddate')
    list_display_links = ('svcarea_name')
    list_per_page = 20

admin.site.register(ServiceArea)
