from django.contrib import admin
from .models import ServiceElement

class SvcElementAdmin(admin.ModelAdmin):
    list_display = ('svcelement_name', 'svcelement_svcarea_fk','svcelement_createdby', 'svcelement_createddate', 'svcelement_modifiedby', 'svcelement_modifieddate')
    list_per_page = 20


admin.site.register(ServiceElement, SvcElementAdmin)