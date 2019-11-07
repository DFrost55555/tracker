from django.contrib import admin
from .models import Vendor,VendorContact,VendorNote,VendorType

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    fields = ('vend_name',)
    ordering = ('vend_name',)      


admin.site.register(Vendor, VendorAdmin)
admin.site.register(VendorContact)
admin.site.register(VendorNote)
admin.site.register(VendorType)
