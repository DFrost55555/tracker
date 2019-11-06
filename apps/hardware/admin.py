from django.contrib import admin
from .models import PortfolioStatus,Hardware,HardwareContact,HardwareNote


# Register your models here.
admin.site.register(PortfolioStatus)
admin.site.register(Hardware)
admin.site.register(HardwareContact)
admin.site.register(HardwareNote)