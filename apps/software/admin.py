from django.contrib import admin
from .models import SWPortfolioStatus,Software,SoftwareContact,SoftwareNote


# Register your models here.
admin.site.register(SWPortfolioStatus)
admin.site.register(Software)
admin.site.register(SoftwareContact)
admin.site.register(SoftwareNote)
