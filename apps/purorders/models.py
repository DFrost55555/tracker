from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from djmoney.models.fields import MoneyField
from apps.customers.models import Customer
from apps.projects.models import Project
from apps.resources.models import Resource, ResourceType
from apps.items.models import Item, ItemType
from apps.suppliers.models import Supplier
from apps.lists.models import POItemType, ChargeUnitType
from apps.approvers.models import Approver
from django.urls import reverse


class POStatus(models.Model):
    posts_id = models.AutoField(primary_key = True)
    posts_name = models.CharField('po status name', max_length=150)
    posts_description = models.CharField('po status description', max_length=2000)
    posts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    posts_createddate = models.DateTimeField(default=timezone.now)
    posts_modifiedby = models.ForeignKey(User, related_name='posts_editor',on_delete=models.SET_NULL, null=True)
    posts_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.posts_name
    
    def get_absolute_url(self):
        return reverse ('posts-detail', kwargs={"pk": self.pk})


class POType(models.Model):
    potyp_id = models.AutoField(primary_key = True)
    potyp_name = models.CharField('po type name', max_length=150)
    potyp_description = models.CharField('po type description', max_length=2000)
    potyp_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    potyp_createddate = models.DateTimeField(default=timezone.now)
    potyp_modifiedby = models.ForeignKey(User, related_name='potyp_editor',on_delete=models.SET_NULL, null=True)
    potyp_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.potyp_name
    
    def get_absolute_url(self):
        return reverse ('potyp-detail', kwargs={"pk": self.pk})
    

class PurchaseOrder(models.Model):
    po_id = models.AutoField(primary_key=True)
    po_reference = models.CharField('PO Reference', max_length=50)
    po_quantity = models.DecimalField('PO Quantity Number', max_digits=10, decimal_places=2, default=0.00)
    po_quantity_type_fk = models.ForeignKey(ChargeUnitType, verbose_name='PO Quantity Type',on_delete=models.SET_NULL, null=True)
    po_cost_value = models.DecimalField('PO Cost Value', max_digits=14, decimal_places=2, default=0.00)
    po_unit_cost = models.DecimalField('PO Unit Cost', max_digits=14, decimal_places=2, default=0.00)
    po_charge_value = models.DecimalField('PO Charge Value', max_digits=14, decimal_places=2, default=0.00)
    po_unit_charge = models.DecimalField('PO Unit Charge', max_digits=14, decimal_places=2, default=0.00)
    po_start_date = models.DateField(verbose_name='Start Date', null=True)
    po_end_date = models.DateField(verbose_name='End Date', null=True)
    po_status_fk = models.ForeignKey(POStatus, verbose_name='PO Status',on_delete=models.SET_NULL, null=True)
    po_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    po_createddate = models.DateTimeField(default=timezone.now)
    po_modifiedby = models.ForeignKey(User, related_name='po_editor',on_delete=models.SET_NULL, null=True)
    po_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.po_reference

    def get_absolute_url(self):
        return reverse ('purorder-detail', kwargs={"pk": self.pk})


class PONote(models.Model):
    ponote_po_fk = models.ForeignKey(PurchaseOrder, verbose_name='Purchase Order', on_delete=models.SET_NULL, null=True)
    ponote_note = models.CharField('PO Note', max_length=2500)
    ponote_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ponote_createddate = models.DateTimeField(default=timezone.now)
    ponote_modifiedby = models.ForeignKey(User, related_name='ponote_editor', on_delete=models.SET_NULL, null=True)
    ponote_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.ponote_note
    
    def get_absolute_url(self):
        return reverse ('ponote-detail', kwargs={"pk": self.pk})
    

class POMatrix(models.Model):
    pomtx_id = models.AutoField(primary_key=True)
    pomtx_po_id = models.ForeignKey(PurchaseOrder, verbose_name='purchase order', on_delete=models.SET_NULL, null=True)
    pomtx_potype_id = models.ForeignKey(POType, verbose_name='purchase order type', on_delete=models.SET_NULL, null=True)
    pomtx_project_fk = models.ForeignKey(Project, verbose_name='project', on_delete=models.SET_NULL, null=True)
    pomtx_customer_fk = models.ForeignKey(Customer, verbose_name="customer", on_delete=models.SET_NULL, null=True)
    pomtx_supplier_fk = models.ForeignKey(Supplier, verbose_name="supplier", on_delete=models.SET_NULL, null=True)
    pomtx_approver_fk = models.ForeignKey(Approver, verbose_name="approver", on_delete=models.SET_NULL, null=True)
    pomtx_apprvd_date = models.DateField(verbose_name='approved date', null=True)
    pomtx_status_fk = models.ForeignKey(POStatus, verbose_name="po status", on_delete=models.SET_NULL, null=True)
    pomtx_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pomtx_createddate = models.DateTimeField(default=timezone.now)
    pomtx_modifiedby = models.ForeignKey(User, related_name='pomtx_editor',on_delete=models.SET_NULL, null=True)
    pomtx_modifieddate = models.DateTimeField(auto_now=True, null=True)
    

class POFiles(models.Model):
    pofile_id = models.AutoField(primary_key=True)
    pofile_po_fk = models.ForeignKey(PurchaseOrder, verbose_name='Purchase Order', on_delete=models.SET_NULL, null=True)
    pofile_name = models.CharField('PO Filename', max_length=255)
    pofile_file = models.FileField(upload_to='pofiles/', max_length=255)
    pofile_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pofile_createddate = models.DateTimeField(default=timezone.now)
    pofile_modifiedby = models.ForeignKey(User, related_name='pofile_editor', on_delete=models.SET_NULL, null=True)
    pofile_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.pofile_name
    
    def get_absolute_url(self):
        return reverse ('pofile-detail', kwargs={"pk": self.pk})
