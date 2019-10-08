from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField('role name', max_length=100)
    role_desc = models.CharField('role description', max_length=2000)
    role_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    role_createddate = models.DateTimeField(default=timezone.now)
    role_modifiedby = models.ForeignKey(User, related_name='role_editor',on_delete=models.SET_NULL, null=True)
    role_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.role_name