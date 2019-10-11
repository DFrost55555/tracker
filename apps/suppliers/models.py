from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class SupplierStatus(models.Model):
    suppsts_id = models.AutoField(primary_key = True)
    suppsts_name = models.CharField('supplier status name', max_length=150)
    suppsts_description = models.CharField('supplier status description', max_length=2000)
    suppsts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    suppsts_createddate = models.DateTimeField(default=timezone.now)
    suppsts_modifiedby = models.ForeignKey(User, related_name='suppsts_editor',on_delete=models.SET_NULL, null=True)
    suppsts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.suppsts_name
    
    def get_absolute_url(self):
        return reverse ('suppsts-detail', kwargs={"pk": self.pk})
    

class Supplier(models.Model):
    supp_id = models.AutoField(primary_key = True)
    supp_name = models.CharField('supplier name', max_length=150)
    supp_description = models.CharField('supplier description', max_length=2000)
    supp_status_fk = models.ForeignKey(SupplierStatus, verbose_name='supplier status', on_delete=models.SET_NULL, null=True)
    supp_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    supp_createddate = models.DateTimeField(default=timezone.now)
    supp_modifiedby = models.ForeignKey(User, related_name='supp_editor',on_delete=models.SET_NULL, null=True)
    supp_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.supp_name
    
    
class SupplierContact(models.Model):
    suppcontact_supplier_fk = models.ForeignKey(Supplier, verbose_name='Supplier', on_delete=models.SET_NULL, null=True)
    suppcontact_firstname = models.CharField('First Name', max_length=150)
    suppcontact_lastname = models.CharField('Last Name', max_length=150)
    suppcontact_role = models.CharField('Role', max_length=150, null=True)
    suppcontact_email = models.EmailField('Email Address', max_length=250)
    suppcontact_telnum = models.CharField('Telephone Number', max_length=150)
    suppcontact_mobnumber = models.CharField('Mobile Number', max_length=150)
    suppcontact_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    suppcontact_createddate = models.DateTimeField(default=timezone.now)
    suppcontact_modifiedby = models.ForeignKey(User, related_name='suppcontact_editor', on_delete=models.SET_NULL, null=True)
    suppcontact_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return '%s %s %s' % (self.suppcontact_lastname, ", ", self.suppcontact_firstname)
    
    def get_absolute_url(self):
        return reverse ('suppcontact-detail', kwargs={"pk": self.pk})
    
    
class SupplierNote(models.Model):
    suppnote_supplier_fk = models.ForeignKey(Supplier, verbose_name='Supplier', on_delete=models.SET_NULL, null=True)
    suppnote_note = models.CharField('Note', max_length=2500)
    suppnote_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    suppnote_createddate = models.DateTimeField(default=timezone.now)
    suppnote_modifiedby = models.ForeignKey(User, related_name='suppnote_editor', on_delete=models.SET_NULL, null=True)
    suppnote_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.suppnote_note
    
    def get_absolute_url(self):
        return reverse ('suppnote-detail', kwargs={"pk": self.pk})
