from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse

from apps.customers.models import Customer
from apps.vendors.models import Vendor
from apps.lists.models import SoftwareCategory, SoftwareStatus, SoftwareClassification, YesNo, TrueFalse, SoftwareFrequency, ApprovalStatus, VendorFrequency


class SWPortfolioStatus(models.Model):
    swportsts_id = models.AutoField(primary_key = True)
    swportsts_name = models.CharField('SW Portfolio Status Name', max_length=150)
    swportsts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    swportsts_createddate = models.DateTimeField(default=timezone.now)
    swportsts_modifiedby = models.ForeignKey(User, related_name='swportsts_editor', on_delete=models.SET_NULL, null=True)
    swportsts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.swportsts_name
        
    def get_absolute_url(self):
        return reverse ('swportsts-detail', kwargs={"pk": self.pk})    


class SWPortfolioCategory(models.Model):
    swportcat_id = models.AutoField(primary_key = True)
    swportcat_name = models.CharField('SW Portfolio Status Name', max_length=150)
    swportcat_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    swportcat_createddate = models.DateTimeField(default=timezone.now)
    swportcat_modifiedby = models.ForeignKey(User, related_name='swportcat_editor', on_delete=models.SET_NULL, null=True)
    swportcat_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.swportcat_name
        
    def get_absolute_url(self):
        return reverse ('swportcat-detail', kwargs={"pk": self.pk})


class Software(models.Model):
    sw_id = models.AutoField(primary_key = True)
    sw_version = models.CharField('Software Version', max_length=250, blank=True, null=True)
    sw_description = models.CharField('Software Description', max_length=250)
    sw_vend_fk = models.ForeignKey(Vendor, verbose_name='Vendor', on_delete=models.SET_NULL, blank=True, null=True)
    sw_progver_code = models.CharField('Version In Progress', max_length=250, blank=True, null=True)
    sw_latestver_code = models.CharField('Latest Available Version', max_length=250, blank=True, null=True)
    sw_cust_notified = models.DateField('Customer Notified', blank=True, null=True) # Customer Notified
    sw_repl_ver = models.CharField('Replacement Software Version', max_length=250, blank=True, null=True)
    sw_repl_desc = models.CharField('Replacement Software Description', max_length=250,blank=True, null=True)
    sw_repl_vend_fk = models.ForeignKey(Vendor, verbose_name='Replacement Vendor', related_name='sw_repl_vend_id', on_delete=models.SET_NULL,blank=True, null=True)
    sw_cust_fk = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.SET_NULL,blank=True, null=True)
    sw_cust_ref = models.CharField('Customer Reference', max_length=250, blank=True, null=True)
    sw_portsts_fk = models.ForeignKey(SWPortfolioStatus, verbose_name='Portfolio Status', on_delete=models.SET_NULL,blank=True, null=True)
    sw_portcat_fk = models.ForeignKey(SWPortfolioCategory, verbose_name='Portfolio Category', on_delete=models.SET_NULL,blank=True, null=True)
    sw_swclass_fk = models.ForeignKey(SoftwareClassification, verbose_name='Software Classification', on_delete=models.SET_NULL,blank=True, null=True)
    sw_swcat_fk = models.ForeignKey(SoftwareCategory, verbose_name='Software Category', on_delete=models.SET_NULL,blank=True, null=True)
    sw_swsts_fk = models.ForeignKey(SoftwareStatus, verbose_name='Software Status', on_delete=models.SET_NULL,blank=True, null=True)
    sw_swfreq_fk = models.ForeignKey(SoftwareFrequency, verbose_name='Software Release Frequency', on_delete=models.SET_NULL,blank=True, null=True)
    sw_vendfreq_fk = models.ForeignKey(VendorFrequency, verbose_name='Vendor Release Frequency', on_delete=models.SET_NULL,blank=True, null=True)    
    sw_int_code = models.CharField('Internal Part Code', max_length=250, blank=True, null=True)
    sw_ext_code = models.CharField('External Part Code', max_length=250, blank=True, null=True)
    sw_eol_date = models.DateField('End of Life', blank=True, null=True) # End of Life
    sw_eow_date = models.DateField('End of Warranty', blank=True, null=True) # End of Warranty
    sw_ems_date = models.DateField('End of Mainstream Support', blank=True, null=True) # End of Mainstream Support
    sw_ees1_date = models.DateField('End of Extended Support - Period One', blank=True, null=True) # End of Extended Support - Period One
    sw_ees2_date = models.DateField('End of Extended Support - Period Two', blank=True, null=True) # End of Extended Support - Period Two
    sw_ees3_date = models.DateField('End of Extended Support - Period Three', blank=True, null=True) # End of Extended Support - Period Three
    sw_see_yn_fk = models.ForeignKey(YesNo, verbose_name='Support End Estimated', on_delete=models.SET_NULL, blank=True, null=True) # Support End Estimated
    sw_plp_txt = models.CharField('Product Lifecycle Policy', max_length=250,blank=True, null=True) # Product Lifecycle Policy
    sw_upd_date = models.DateField('Info Update', blank=True, null=True)
    sw_int_reference = models.CharField('Internal Reference', max_length=250, blank=True, null=True)
    sw_createdby = models.ForeignKey(User, verbose_name='Created By', on_delete=models.SET_NULL, blank=True, null=True)
    sw_createddate = models.DateTimeField(default=timezone.now)
    sw_modifiedby = models.ForeignKey(User, verbose_name='Modified By', related_name='sw_editor', on_delete=models.SET_NULL,blank=True, null=True)
    sw_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.sw_description
 
    
    def get_absolute_url(self):
        return reverse ('software-detail', kwargs={"pk": self.pk})
    
    
class SoftwareContact(models.Model):
    swcontact_id = models.AutoField(primary_key = True)
    swcontact_sw_fk = models.ForeignKey(Software, verbose_name='Software', on_delete=models.SET_NULL, null=True)
    swcontact_firstname = models.CharField('First Name', max_length=150, null=True)
    swcontact_lastname = models.CharField('Last Name', max_length=150, null=True)
    swcontact_role = models.CharField('Role', max_length=150, blank=True, null=True)
    swcontact_email = models.EmailField('Email Address', max_length=250, blank=True, null=True)
    swcontact_telnum = models.CharField('Telephone Number', max_length=150, blank=True, null=True)
    swcontact_mobnumber = models.CharField('Mobile Number', max_length=150, blank=True, null=True)
    swcontact_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    swcontact_createddate = models.DateTimeField(default=timezone.now)
    swcontact_modifiedby = models.ForeignKey(User, related_name='swcontact_editor', on_delete=models.SET_NULL, null=True)
    swcontact_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.swcontact_email
    objects = models.Manager()
    
    def get_absolute_url(self):
        return reverse ('swcontact-detail', kwargs={"pk": self.pk})
    
class SoftwareNote(models.Model):
    swnote_id = models.AutoField(primary_key = True)
    swnote_sw_fk = models.ForeignKey(Software, verbose_name='Software', on_delete=models.SET_NULL, null=True)
    swnote_note = models.CharField('Note', max_length=2500)
    swnote_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    swnote_createddate = models.DateTimeField(default=timezone.now)
    swnote_modifiedby = models.ForeignKey(User, related_name='swnote_editor', on_delete=models.SET_NULL, null=True)
    swnote_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.swnote_note
    objects = models.Manager()
    
    def get_absolute_url(self):
        return reverse ('swnote-detail', kwargs={"pk": self.pk})



