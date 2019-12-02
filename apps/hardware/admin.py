from django.contrib import admin
from .models import PortfolioStatus,Hardware,HardwareContact,HardwareNote, HardwareMatrix, PortfolioCategory


# Register your models here.
admin.site.register(PortfolioStatus)
admin.site.register(PortfolioCategory)
admin.site.register(Hardware)
admin.site.register(HardwareContact)
admin.site.register(HardwareNote)
admin.site.register(HardwareMatrix)