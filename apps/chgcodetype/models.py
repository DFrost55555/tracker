from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class ChgCodeType(models.Model):
    chgcodetype_name = models.CharField('Charge Code Type Name', max_length=150)
    chgcodetype_description = models.CharField('Description', max_length=2000)
    chgcodetype_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chgcodetype_createddate = models.DateTimeField(default=timezone.now)
    chgcodetype_modifiedby = models.ForeignKey(User, related_name='chgcodetype_editor',on_delete=models.SET_NULL, null=True)
    chgcodetype_modifieddate = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.chgcodetype_name
