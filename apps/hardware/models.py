from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse

from apps.customers.models import Customer
from apps.vendors.models import Vendor
from apps.lists.models import HardwareCategory,HardwareStatus


class PortfolioStatus(models.Model):
    portsts_id = models.AutoField(primary_key = True)
    portsts_name = models.CharField('Portfolio Status Name', max_length=150)
    portsts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    portsts_createddate = models.DateTimeField(default=timezone.now)
    portsts_modifiedby = models.ForeignKey(User, related_name='portsts_editor', on_delete=models.SET_NULL, null=True)
    portsts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.portsts_name
        
    def get_absolute_url(self):
        return reverse ('portsts-detail', kwargs={"pk": self.pk})    


class Hardware(models.Model):
    hw_id = models.AutoField(primary_key = True)
    hw_description = models.CharField('Hardware Description', max_length=250)
    hw_cust_fk = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    hw_portsts_fk = models.ForeignKey(PortfolioStatus, on_delete=models.SET_NULL, null=True)
    hw_hwcat_fk = models.ForeignKey(HardwareCategory, on_delete=models.SET_NULL, null=True)
    hw_hwsts_fk = models.ForeignKey(HardwareStatus, on_delete=models.SET_NULL, null=True)
    hw_int_code = models.CharField('Internal Part Code', max_length=250)
    hw_ext_code = models.CharField('External Part Code', max_length=250)
    hw_eol_date = models.DateTimeField(null=True)
    hw_upd_date = models.DateTimeField(null=True)
    hw_int_reference = models.CharField('Internal Reference', max_length=250)
    hw_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hw_createddate = models.DateTimeField(default=timezone.now)
    hw_modifiedby = models.ForeignKey(User, related_name='hw_editor', on_delete=models.SET_NULL, null=True)
    hw_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.hw_description
    objects = models.Manager()
    
    def get_absolute_url(self):
        return reverse ('hardware-detail', kwargs={"pk": self.pk})
    
    
class HardwareContact(models.Model):
    hwcontact_id = models.AutoField(primary_key = True)
    hwcontact_hw_fk = models.ForeignKey(Hardware, verbose_name='Hardware', on_delete=models.SET_NULL, null=True)
    hwcontact_firstname = models.CharField('First Name', max_length=150)
    hwcontact_lastname = models.CharField('Last Name', max_length=150)
    hwcontact_role = models.CharField('Role', max_length=150, null=True)
    hwcontact_email = models.EmailField('Email Address', max_length=250)
    hwcontact_telnum = models.CharField('Telephone Number', max_length=150)
    hwcontact_mobnumber = models.CharField('Mobile Number', max_length=150)
    hwcontact_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hwcontact_createddate = models.DateTimeField(default=timezone.now)
    hwcontact_modifiedby = models.ForeignKey(User, related_name='hwcontact_editor', on_delete=models.SET_NULL, null=True)
    hwcontact_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.hwcontact_email
    objects = models.Manager()
    
    def get_absolute_url(self):
        return reverse ('hwcontact-detail', kwargs={"pk": self.pk})
    
class HardwareNote(models.Model):
    hwnote_id = models.AutoField(primary_key = True)
    hwnote_hw_fk = models.ForeignKey(Hardware, verbose_name='Hardware', on_delete=models.SET_NULL, null=True)
    hwnote_note = models.CharField('Note', max_length=2500)
    hwnote_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hwnote_createddate = models.DateTimeField(default=timezone.now)
    hwnote_modifiedby = models.ForeignKey(User, related_name='hwnote_editor', on_delete=models.SET_NULL, null=True)
    hwnote_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.hwnote_note
    objects = models.Manager()
    
    def get_absolute_url(self):
        return reverse ('hwnote-detail', kwargs={"pk": self.pk})



