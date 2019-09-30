from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class StatusType(models.Model):
    statustype_name = models.CharField('Status Type Name', max_length=150)
    statustype_description = models.CharField('Description', max_length=2000)
    statustype_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    statustype_createddate = models.DateTimeField(default=timezone.now)
    statustype_modifiedby = models.ForeignKey(User, related_name='ststype_editor',on_delete=models.SET_NULL, null=True)
    statustype_modifieddate = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.statustype_name
