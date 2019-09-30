from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.svcarea.models import ServiceArea
from django.urls import reverse

class ServiceElement(models.Model):
    svcelement_name = models.CharField('Service Element Name', max_length=150)
    svcelement_svcarea_fk = models.ForeignKey(ServiceArea, verbose_name='Service Area', on_delete=models.SET_NULL, null=True)
    svcelement_description = models.CharField('Description', max_length=2000)
    svcelement_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    svcelement_createddate = models.DateTimeField(default=timezone.now)
    svcelement_modifiedby = models.ForeignKey(User, related_name='svcelement_editor',on_delete=models.SET_NULL, null=True)
    svcelement_modifieddate = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.svcelement_name
