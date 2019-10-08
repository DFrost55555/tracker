from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Supplier(models.Model):
    supp_id = models.AutoField(primary_key = True)
    supp_name = models.CharField('supplier name', max_length=150)
    supp_description = models.CharField('supplier description', max_length=2000)
    supp_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    supp_createddate = models.DateTimeField(default=timezone.now)
    supp_modifiedby = models.ForeignKey(User, related_name='supp_editor',on_delete=models.SET_NULL, null=True)
    supp_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.supp_name
