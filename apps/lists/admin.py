from django.contrib import admin
from .models import Location, ProjectStatus, ResourceStatus, ChargeCodeType, ChargeUnitType

admin.site.register(Location)
admin.site.register(ProjectStatus)
admin.site.register(ResourceStatus)
admin.site.register(ChargeCodeType)
admin.site.register(ChargeUnitType)