from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Location(models.Model):
    loc_id = models.AutoField(primary_key = True)
    loc_name = models.CharField('location name', max_length=150)
    loc_description = models.CharField('location description', max_length=2000)
    loc_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    loc_createddate = models.DateTimeField(default=timezone.now)
    loc_modifiedby = models.ForeignKey(User, related_name='loc_editor',on_delete=models.SET_NULL, null=True)
    loc_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.loc_name
    

class ProjectStatus(models.Model):
    prjsts_id = models.AutoField(primary_key = True)
    prjsts_name = models.CharField('location name', max_length=150)
    prjsts_description = models.CharField('location description', max_length=2000)
    prjsts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    prjsts_createddate = models.DateTimeField(default=timezone.now)
    prjsts_modifiedby = models.ForeignKey(User, related_name='prjsts_editor',on_delete=models.SET_NULL, null=True)
    prjsts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.prjsts_name
    

class ChargeCodeType(models.Model):
    cct_id = models.AutoField(primary_key = True)
    cct_name = models.CharField('location name', max_length=150)
    cct_description = models.CharField('location description', max_length=2000)
    cct_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cct_createddate = models.DateTimeField(default=timezone.now)
    cct_modifiedby = models.ForeignKey(User, related_name='cct_editor',on_delete=models.SET_NULL, null=True)
    cct_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.cct_name
    

class ChargeUnitType(models.Model):
    cut_id = models.AutoField(primary_key = True)
    cut_name = models.CharField('location name', max_length=150)
    cut_description = models.CharField('location description', max_length=2000)
    cut_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cut_createddate = models.DateTimeField(default=timezone.now)
    cut_modifiedby = models.ForeignKey(User, related_name='cut_editor',on_delete=models.SET_NULL, null=True)
    cut_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.cut_name
    

class ResourceStatus(models.Model):
    ressts_id = models.AutoField(primary_key = True)
    ressts_name = models.CharField('location name', max_length=150)
    ressts_description = models.CharField('location description', max_length=2000)
    ressts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ressts_createddate = models.DateTimeField(default=timezone.now)
    ressts_modifiedby = models.ForeignKey(User, related_name='ressts_editor',on_delete=models.SET_NULL, null=True)
    ressts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.ressts_name