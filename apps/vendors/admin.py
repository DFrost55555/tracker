from django.contrib import admin
from .models import Vendor,VendorContact,VendorNote,VendorType

# Register your models here.

admin.site.register(Vendor)
admin.site.register(VendorContact)
admin.site.register(VendorNote)
admin.site.register(VendorType)
