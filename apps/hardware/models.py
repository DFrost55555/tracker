from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse

from apps.customers.models import Customer
from apps.vendors.models import Vendor
from apps.lists.models import HardwareCategory, HardwareStatus, YesNo


class PortfolioStatus(models.Model):
    portsts_id = models.AutoField(primary_key = True)
    portsts_name = models.CharField('Portfolio Status Name', max_length=250)
    portsts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    portsts_createddate = models.DateTimeField(default=timezone.now)
    portsts_modifiedby = models.ForeignKey(User, related_name='portsts_editor', on_delete=models.SET_NULL, null=True)
    portsts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.portsts_name
        
    def get_absolute_url(self):
        return reverse ('portsts-detail', kwargs={"pk": self.pk})
    
    
class PortfolioCategory(models.Model):
    portcat_id = models.AutoField(primary_key = True)
    portcat_name = models.CharField('Portfolio Category Name', max_length=250)
    portcat_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    portcat_createddate = models.DateTimeField(default=timezone.now)
    portcat_modifiedby = models.ForeignKey(User, related_name='portcat_editor', on_delete=models.SET_NULL, null=True)
    portcat_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.portsts_name
        
    def get_absolute_url(self):
        return reverse ('portsts-detail', kwargs={"pk": self.pk})   


class Hardware(models.Model):
    hw_id = models.AutoField(primary_key = True)
    hw_description = models.CharField('Hardware Description', max_length=250)
    hw_vend_fk = models.ForeignKey(Vendor, verbose_name='Vendor', on_delete=models.SET_NULL, blank=True, null=True)
    hw_repl_desc = models.CharField('Replacement Hardware Description', max_length=250,blank=True, null=True)
    hw_repl_vend_fk = models.ForeignKey(Vendor, verbose_name='Replacement Vendor', related_name='hw_repl_vend_id', on_delete=models.SET_NULL,blank=True, null=True)
    hw_cust_fk = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.SET_NULL,blank=True, null=True)
    hw_portsts_fk = models.ForeignKey(PortfolioStatus, verbose_name='Portfolio Status', on_delete=models.SET_NULL,blank=True, null=True)
    hw_hwcat_fk = models.ForeignKey(HardwareCategory, verbose_name='Hardware Category', on_delete=models.SET_NULL,blank=True, null=True)
    hw_hwsts_fk = models.ForeignKey(HardwareStatus, verbose_name='Hardware Status', on_delete=models.SET_NULL,blank=True, null=True)
    hw_int_code = models.CharField('Internal Part Code', max_length=250, blank=True, null=True)
    hw_ext_code = models.CharField('External Part Code', max_length=250, blank=True, null=True)
    hw_eol_date = models.DateField('End of Life', blank=True, null=True) # End of Life
    hw_eow_date = models.DateField('End of Warranty', blank=True, null=True) # End of Warranty
    hw_ems_date = models.DateField('End of Mainstream Support', blank=True, null=True) # End of Mainstream Support
    hw_ees1_date = models.DateField('End of Extended Support - Period One', blank=True, null=True) # End of Extended Support - Period One
    hw_ees2_date = models.DateField('End of Extended Support - Period Two', blank=True, null=True) # End of Extended Support - Period Two
    hw_ees3_date = models.DateField('End of Extended Support - Period Three', blank=True, null=True) # End of Extended Support - Period Three
    hw_see_yn_fk = models.ForeignKey(YesNo, verbose_name='Support End Estimated', on_delete=models.SET_NULL,blank=True, null=True) # Support End Estimated
    hw_plp_txt = models.CharField('Product Lifecycle Policy', max_length=250,blank=True, null=True) # Product Lifecycle Policy
    hw_upd_date = models.DateField('Info Update', blank=True, null=True)
    hw_int_reference = models.CharField('Internal Reference', max_length=250, blank=True, null=True)
    hw_createdby = models.ForeignKey(User, verbose_name='Created By', on_delete=models.SET_NULL, blank=True, null=True)
    hw_createddate = models.DateTimeField(default=timezone.now)
    hw_modifiedby = models.ForeignKey(User, verbose_name='Modified By', related_name='hw_editor', on_delete=models.SET_NULL,blank=True, null=True)
    hw_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.hw_description
 
    
    def get_absolute_url(self):
        return reverse ('hardware-detail', kwargs={"pk": self.pk})
    
    
class HardwareContact(models.Model):
    hwcontact_id = models.AutoField(primary_key = True)
    hwcontact_hw_fk = models.ForeignKey(Hardware, verbose_name='Hardware', on_delete=models.SET_NULL, null=True)
    hwcontact_firstname = models.CharField('First Name', max_length=150, null=True)
    hwcontact_lastname = models.CharField('Last Name', max_length=150, null=True)
    hwcontact_role = models.CharField('Role', max_length=150, blank=True, null=True)
    hwcontact_email = models.EmailField('Email Address', max_length=250, blank=True, null=True)
    hwcontact_telnum = models.CharField('Telephone Number', max_length=150, blank=True, null=True)
    hwcontact_mobnumber = models.CharField('Mobile Number', max_length=150, blank=True, null=True)
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
    
    
class HardwareMatrix(models.Model):
    hwmtx_id = models.AutoField(primary_key = True)
    hwmtx_hw_fk = models.ForeignKey(Hardware, verbose_name='Hardware Product', on_delete=models.SET_NULL, blank=True, null=True)
    hwmtx_cust_fk = models.ForeignKey(Customer, verbose_name='Software Customer', on_delete=models.SET_NULL,blank=True, null=True)
    hwmtx_cust_ref = models.CharField('Customer Reference', max_length=250, blank=True, null=True)
    hwmtx_portsts_fk = models.ForeignKey(PortfolioStatus, verbose_name='Portfolio Status', on_delete=models.SET_NULL,blank=True, null=True)
    hwmtx_portcat_fk = models.ForeignKey(PortfolioCategory, verbose_name='Portfolio Category', on_delete=models.SET_NULL,blank=True, null=True)
    hwmtx_hwcat_fk = models.ForeignKey(HardwareCategory, verbose_name='Hardware Category', on_delete=models.SET_NULL,blank=True, null=True)
    hwmtx_hwsts_fk = models.ForeignKey(HardwareStatus, verbose_name='Hardware Status', on_delete=models.SET_NULL,blank=True, null=True)
    hwmtx_cust_code = models.CharField('Customer Part Code', max_length=250, blank=True, null=True)
    hwmtx_cust_ref = models.CharField('Customer Reference', max_length=250, blank=True, null=True)   
    hwmtx_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hwmtx_createddate = models.DateTimeField(default=timezone.now)
    hwmtx_modifiedby = models.ForeignKey(User, related_name='hwmtx_editor', on_delete=models.SET_NULL, null=True)
    hwmtx_modifieddate = models.DateTimeField(auto_now=True, null=True)



