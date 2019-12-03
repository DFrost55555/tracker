from django.contrib import admin
from .models import SWPortfolioStatus,Software,SoftwareContact,SoftwareNote, SWPortfolioCategory,SoftwareVendor, SWVendorContact, SWVendorNote, SoftwareMatrix


# Register your models here.

class SoftwareMatrixAdmin(admin.ModelAdmin):
    list_display = ('swmtx_id', 'swmtx_hw_fk','swmtx_cust_fk','swmtx_portsts_fk','swmtx_portcat_fk')
    list_display_links = ('swmtx_sw_fk')
    list_per_page = 15

admin.site.register(SWPortfolioStatus)
admin.site.register(Software)
admin.site.register(SoftwareContact)
admin.site.register(SoftwareNote)
admin.site.register(SWPortfolioCategory)
admin.site.register(SoftwareVendor)
admin.site.register(SWVendorContact)
admin.site.register(SWVendorNote)
admin.site.register(SoftwareMatrix, SoftwareMatrixAdmin)
