from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class ServiceArea(models.Model):
    svcarea_name = models.CharField('Service Area Name', max_length=150)
    svcarea_description = models.CharField('Description', max_length=2000)
    svcarea_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    svcarea_createddate = models.DateTimeField(default=timezone.now)
    svcarea_modifiedby = models.ForeignKey(User, related_name='svcarea_editor',on_delete=models.SET_NULL, null=True)
    svcarea_modifieddate = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.svcarea_name
