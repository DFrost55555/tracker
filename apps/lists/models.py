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
    prjsts_name = models.CharField('project status name', max_length=150)
    prjsts_description = models.CharField('project status description', max_length=2000)
    prjsts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    prjsts_createddate = models.DateTimeField(default=timezone.now)
    prjsts_modifiedby = models.ForeignKey(User, related_name='prjsts_editor',on_delete=models.SET_NULL, null=True)
    prjsts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.prjsts_name
    

class ChargeCodeType(models.Model):
    cct_id = models.AutoField(primary_key = True)
    cct_name = models.CharField('charge code type name', max_length=150)
    cct_description = models.CharField('charge code type description', max_length=2000)
    cct_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cct_createddate = models.DateTimeField(default=timezone.now)
    cct_modifiedby = models.ForeignKey(User, related_name='cct_editor',on_delete=models.SET_NULL, null=True)
    cct_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.cct_name
    

class ChargeUnitType(models.Model):
    cut_id = models.AutoField(primary_key = True)
    cut_name = models.CharField('charge unit type name', max_length=150)
    cut_description = models.CharField('charge unit type description', max_length=2000)
    cut_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cut_createddate = models.DateTimeField(default=timezone.now)
    cut_modifiedby = models.ForeignKey(User, related_name='cut_editor',on_delete=models.SET_NULL, null=True)
    cut_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.cut_name
    

class ResourceStatus(models.Model):
    ressts_id = models.AutoField(primary_key = True)
    ressts_name = models.CharField('resource status name', max_length=150)
    ressts_description = models.CharField('resource status description', max_length=2000)
    ressts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ressts_createddate = models.DateTimeField(default=timezone.now)
    ressts_modifiedby = models.ForeignKey(User, related_name='ressts_editor',on_delete=models.SET_NULL, null=True)
    ressts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.ressts_name
    
        
class POItemType(models.Model):
    poit_id = models.AutoField(primary_key = True)
    poit_name = models.CharField('po item type name', max_length=150)
    poit_description = models.CharField('po item type description', max_length=2000)
    poit_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    poit_createddate = models.DateTimeField(default=timezone.now)
    poit_modifiedby = models.ForeignKey(User, related_name='poit_editor',on_delete=models.SET_NULL, null=True)
    poit_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.poit_name
    
        
class RAGStatus(models.Model):
    ragsts_id = models.AutoField(primary_key = True)
    ragsts_name = models.CharField('rag status name', max_length=150)
    ragsts_description = models.CharField('rag status description', max_length=2000)
    ragsts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ragsts_createddate = models.DateTimeField(default=timezone.now)
    ragsts_modifiedby = models.ForeignKey(User, related_name='ragsts_editor',on_delete=models.SET_NULL, null=True)
    ragsts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.ragsts_name
    
        
class RAIDStatus(models.Model):
    raidsts_id = models.AutoField(primary_key = True)
    raidsts_name = models.CharField('raid status name', max_length=150)
    raidsts_description = models.CharField('raid status description', max_length=2000)
    raidsts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    raidsts_createddate = models.DateTimeField(default=timezone.now)
    raidsts_modifiedby = models.ForeignKey(User, related_name='raidsts_editor',on_delete=models.SET_NULL, null=True)
    raidsts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.raidsts_name
    
        
class RAIDType(models.Model):
    raidtyp_id = models.AutoField(primary_key = True)
    raidtyp_name = models.CharField('raid type name', max_length=150)
    raidtyp_description = models.CharField('raid type description', max_length=2000)
    raidtyp_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    raidtyp_createddate = models.DateTimeField(default=timezone.now)
    raidtyp_modifiedby = models.ForeignKey(User, related_name='raidtyp_editor',on_delete=models.SET_NULL, null=True)
    raidtyp_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.raidtyp_name
    
        
class ListPriority(models.Model):
    ltprty_id = models.AutoField(primary_key = True)
    ltprty_name = models.CharField('list priority name', max_length=150)
    ltprty_description = models.CharField('list priority description', max_length=2000)
    ltprty_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ltprty_createddate = models.DateTimeField(default=timezone.now)
    ltprty_modifiedby = models.ForeignKey(User, related_name='ltprty_editor',on_delete=models.SET_NULL, null=True)
    ltprty_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.ltprty_name
    

class HardwareCategory(models.Model):
    hwcat_id = models.AutoField(primary_key = True)
    hwcat_name = models.CharField('hardware category name', max_length=150)
    hwcat_description = models.CharField('hardware category description', max_length=2000)
    hwcat_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hwcat_createddate = models.DateTimeField(default=timezone.now)
    hwcat_modifiedby = models.ForeignKey(User, related_name='hwcat_editor',on_delete=models.SET_NULL, null=True)
    hwcat_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.hwcat_name


class HardwareStatus(models.Model):
    hwsts_id = models.AutoField(primary_key = True)
    hwsts_name = models.CharField('hardware status name', max_length=150)
    hwsts_description = models.CharField('hardware status description', max_length=2000)
    hwsts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hwsts_createddate = models.DateTimeField(default=timezone.now)
    hwsts_modifiedby = models.ForeignKey(User, related_name='hwsts_editor',on_delete=models.SET_NULL, null=True)
    hwsts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.hwsts_name
    
    
class SoftwareCategory(models.Model):
    swcat_id = models.AutoField(primary_key = True)
    swcat_name = models.CharField('software category name', max_length=150)
    swcat_description = models.CharField('software category description', max_length=2000)
    swcat_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    swcat_createddate = models.DateTimeField(default=timezone.now)
    swcat_modifiedby = models.ForeignKey(User, related_name='swcat_editor',on_delete=models.SET_NULL, null=True)
    swcat_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.swcat_name


class SoftwareStatus(models.Model):
    swsts_id = models.AutoField(primary_key = True)
    swsts_name = models.CharField('software status name', max_length=150)
    swsts_description = models.CharField('software status description', max_length=2000)
    swsts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    swsts_createddate = models.DateTimeField(default=timezone.now)
    swsts_modifiedby = models.ForeignKey(User, related_name='swsts_editor',on_delete=models.SET_NULL, null=True)
    swsts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.swsts_name


class SoftwareClassification(models.Model):
    swclass_id = models.AutoField(primary_key = True)
    swclass_name = models.CharField('software classification  name', max_length=150)
    swclass_description = models.CharField('software classification description', max_length=2000)
    swclass_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    swclass_createddate = models.DateTimeField(default=timezone.now)
    swclass_modifiedby = models.ForeignKey(User, related_name='swclass_editor',on_delete=models.SET_NULL, null=True)
    swclass_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.swclass_name
    
    
class ProductType(models.Model):
    prdtype_id = models.AutoField(primary_key = True)
    prdtype_name = models.CharField('product type name', max_length=150)
    prdtype_description = models.CharField('product type description', max_length=2000)
    prdtype_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    prdtype_createddate = models.DateTimeField(default=timezone.now)
    prdtype_modifiedby = models.ForeignKey(User, related_name='prdtype_editor',on_delete=models.SET_NULL, null=True)
    prdtype_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.prdtype_name
    
class YesNo(models.Model):
    yesno_id = models.AutoField(primary_key = True)
    yesno_text = models.CharField('yes no', max_length=10)
    yesno_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    yesno_createddate = models.DateTimeField(default=timezone.now)
    yesno_modifiedby = models.ForeignKey(User, related_name='yesno_editor',on_delete=models.SET_NULL, null=True)
    yesno_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.yesno_text
    
class TrueFalse(models.Model):
    tf_id = models.AutoField(primary_key = True)
    tf_text = models.CharField('yes no', max_length=10)
    tf_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tf_createddate = models.DateTimeField(default=timezone.now)
    tf_modifiedby = models.ForeignKey(User, related_name='tf_editor',on_delete=models.SET_NULL, null=True)
    tf_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.tf_text
    
class ApprovalStatus(models.Model):
    apprsts_id = models.AutoField(primary_key = True)
    apprsts_text = models.CharField('Approval Status', max_length=50)
    apprsts_desc = models.CharField('Approval Status Description', max_length=2500, blank=True, null=True)
    apprsts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    apprsts_createddate = models.DateTimeField(default=timezone.now)
    apprsts_modifiedby = models.ForeignKey(User, related_name='apprsts_editor',on_delete=models.SET_NULL, null=True)
    apprsts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.apprsts_text

class SoftwareFrequency(models.Model):
    swfreq_id = models.AutoField(primary_key = True)
    swfreq_text = models.CharField('Agreed Release Frequency', max_length=250)
    swfreq_desc = models.CharField('Agreed Release Frequency Description', max_length=2500, blank=True, null=True)
    swfreq_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    swfreq_createddate = models.DateTimeField(default=timezone.now)
    swfreq_modifiedby = models.ForeignKey(User, related_name='swfreq_editor',on_delete=models.SET_NULL, null=True)
    swfreq_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.swfreq_text
    
class VendorFrequency(models.Model):
    vendfreq_id = models.AutoField(primary_key = True)
    vendfreq_text = models.CharField('Vendor Release Frequency', max_length=250)
    vendfreq_desc = models.CharField('Vendor Release Frequency Description', max_length=2500, blank=True, null=True)
    vendfreq_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vendfreq_createddate = models.DateTimeField(default=timezone.now)
    vendfreq_modifiedby = models.ForeignKey(User, related_name='vendfreq_editor',on_delete=models.SET_NULL, null=True)
    vendfreq_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.vendfreq_text