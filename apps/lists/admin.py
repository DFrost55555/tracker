from django.contrib import admin
from .models import Location, ProjectStatus, ResourceStatus, ChargeCodeType, ChargeUnitType, POItemType,RAGStatus,ListPriority,RAIDStatus,RAIDType,HardwareCategory,HardwareStatus,SoftwareCategory,SoftwareStatus,SoftwareClassification,ProductType, YesNo, TrueFalse, ApprovalStatus

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
admin.site.register(HardwareCategory)
admin.site.register(HardwareStatus)
admin.site.register(SoftwareCategory)
admin.site.register(SoftwareStatus)
admin.site.register(SoftwareClassification)
admin.site.register(ProductType)
admin.site.register(YesNo)
admin.site.register(TrueFalse)
admin.site.register(ApprovalStatus)
ApprovalStatus