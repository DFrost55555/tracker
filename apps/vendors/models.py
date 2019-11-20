from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse
    

class VendorType(models.Model):
    vendtype_id = models.AutoField(primary_key = True)
    vendtype_name = models.CharField('Vendor Type Name', max_length=150)
    vendtype_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vendtype_createddate = models.DateTimeField(default=timezone.now)
    vendtype_modifiedby = models.ForeignKey(User, related_name='vendtype_editor', on_delete=models.SET_NULL, null=True)
    vendtype_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.vendtype_name
        
    def get_absolute_url(self):
        return reverse ('vendtype-detail', kwargs={"pk": self.pk})


class Vendor(models.Model):
    vend_id = models.AutoField(primary_key = True)
    vend_name = models.CharField('Vendor Name', max_length=150)
    vend_type_fk = models.ForeignKey(VendorType, verbose_name='Vendor Type', on_delete=models.SET_NULL, blank=True, null=True)
    vend_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vend_createddate = models.DateTimeField(default=timezone.now)
    vend_modifiedby = models.ForeignKey(User, related_name='vend_editor', on_delete=models.SET_NULL, null=True)
    vend_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.vend_name
    objects = models.Manager()
    
    def get_absolute_url(self):
        return reverse ('Vendor-detail', kwargs={"pk": self.pk})
    
    
class VendorContact(models.Model):
    vendcontact_id = models.AutoField(primary_key = True)
    vendcontact_vendor_fk = models.ForeignKey(Vendor, verbose_name='Vendor', on_delete=models.SET_NULL, null=True)
    vendcontact_firstname = models.CharField('First Name', max_length=150)
    vendcontact_lastname = models.CharField('Last Name', max_length=150)
    vendcontact_role = models.CharField('Role', max_length=150, null=True)
    vendcontact_email = models.EmailField('Email Address', max_length=250)
    vendcontact_telnum = models.CharField('Telephone Number', max_length=150)
    vendcontact_mobnumber = models.CharField('Mobile Number', max_length=150)
    vendcontact_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vendcontact_createddate = models.DateTimeField(default=timezone.now)
    vendcontact_modifiedby = models.ForeignKey(User, related_name='vendcontact_editor', on_delete=models.SET_NULL, null=True)
    vendcontact_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.vendcontact_email
    objects = models.Manager()
    
    def get_absolute_url(self):
        return reverse ('vendcontact-detail', kwargs={"pk": self.pk})
    
class VendorNote(models.Model):
    vendnote_id = models.AutoField(primary_key = True)
    vendnote_vend_fk = models.ForeignKey(Vendor, verbose_name='Vendor', on_delete=models.SET_NULL, null=True)
    vendnote_note = models.CharField('Note', max_length=2500)
    vendnote_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vendnote_createddate = models.DateTimeField(default=timezone.now)
    vendnote_modifiedby = models.ForeignKey(User, related_name='vendnote_editor', on_delete=models.SET_NULL, null=True)
    vendnote_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.vendnote_note
    objects = models.Manager()
    
    def get_absolute_url(self):
        return reverse ('vendnote-detail', kwargs={"pk": self.pk})
