from django.contrib import admin
from .models import PurchaseOrder, POMatrix, PONote, POStatus, POType, POFiles

admin.site.register(PurchaseOrder)
admin.site.register(POMatrix)
admin.site.register(PONote)
admin.site.register(POStatus)
admin.site.register(POType)
admin.site.register(POFiles)