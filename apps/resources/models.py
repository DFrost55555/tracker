from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class ResourceType(models.Model):
    restype_id = models.AutoField(primary_key=True)
    restype_name = models.CharField('resource type', max_length=100)
    restype_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    restype_createddate = models.DateTimeField(default=timezone.now)
    restype_modifiedby = models.ForeignKey(User, related_name='restype_editor',on_delete=models.SET_NULL, null=True)
    restype_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.restype_name

    def get_absolute_url(self):
        return reverse ('restype-detail', kwargs={"pk": self.pk})
    

class Resource(models.Model):
    res_id = models.AutoField(primary_key=True)
    res_firstname = models.CharField('firstname', max_length=100)
    res_lastname = models.CharField('lastname', max_length=100)
    res_resource_type = models.ForeignKey(ResourceType, verbose_name='resource type', on_delete=models.SET_NULL, null=True)
    res_emp_ref = models.CharField('employee reference', max_length=50)
    res_networkid = models.CharField('network id', max_length=50)
    res_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    res_createddate = models.DateTimeField(default=timezone.now)
    res_modifiedby = models.ForeignKey(User, related_name='res_editor',on_delete=models.SET_NULL, null=True)
    res_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.res_lastname and self.res_firstname

    def get_absolute_url(self):
        return reverse ('resource-detail', kwargs={"pk": self.pk})
    
    

