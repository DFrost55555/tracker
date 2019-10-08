from django.contrib import admin
from .models import Location, ProjectStatus, ResourceStatus, ChargeCodeType, ChargeUnitType, POItemType,RAGStatus,ListPriority,RAIDStatus,RAIDType

admin.site.register(Location)
admin.site.register(ProjectStatus)
admin.site.register(ResourceStatus)
admin.site.register(ChargeCodeType)
admin.site.register(ChargeUnitType)
admin.site.register(POItemType)
admin.site.register(RAGStatus)
admin.site.register(ListPriority)
admin.site.register(RAIDStatus)
admin.site.register(RAIDType)