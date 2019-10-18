from django.contrib import admin
from .models import Invoice, INVMatrix, INVNote, INVStatus, INVType

admin.site.register(Invoice)
admin.site.register(INVMatrix)
admin.site.register(INVNote)
admin.site.register(INVStatus)
admin.site.register(INVType)
