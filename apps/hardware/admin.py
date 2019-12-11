from django.contrib import admin
from .models import PortfolioStatus,Hardware,HardwareContact,HardwareNote, HardwareMatrix, PortfolioCategory


# Register your models here.

class HardwareMatrixAdmin(admin.ModelAdmin):
    list_display = ('hwmtx_id', 'hwmtx_hw_fk','hwmtx_cust_fk','hwmtx_portsts_fk','hwmtx_portcat_fk')
    list_display_links = ('hwmtx_hw_fk', 'hwmtx_cust_fk','hwmtx_portsts_fk','hwmtx_portcat_fk')
    list_per_page = 15

admin.site.register(PortfolioStatus)
admin.site.register(PortfolioCategory)
admin.site.register(Hardware)
admin.site.register(HardwareContact)
admin.site.register(HardwareNote)
admin.site.register(HardwareMatrix, HardwareMatrixAdmin)