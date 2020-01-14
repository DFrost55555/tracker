from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from apps.purorders.models import PurchaseOrder
from apps.customers.models import Customer
from apps.projects.models import Project
from apps.resources.models import Resource, ResourceType
from apps.items.models import Item, ItemType
from apps.suppliers.models import Supplier
from apps.lists.models import POItemType, ChargeUnitType
from apps.approvers.models import Approver
from django.urls import reverse
from djmoney.models.fields import MoneyField


class INVStatus(models.Model):
    invsts_id = models.AutoField(primary_key=True)
    invsts_name = models.CharField('invoice status name', max_length=150)
    invsts_description = models.CharField('invoice status description', max_length=2000)
    invsts_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    invsts_createddate = models.DateTimeField(default=timezone.now)
    invsts_modifiedby = models.ForeignKey(User, related_name='invsts_editor', on_delete=models.SET_NULL, null=True)
    invsts_modifieddate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.invsts_name

    def get_absolute_url(self):
        return reverse('invsts-detail', kwargs={"pk": self.pk})


class INVType(models.Model):
    invtyp_id = models.AutoField(primary_key=True)
    invtyp_name = models.CharField('inv type name', max_length=150)
    invtyp_description = models.CharField('inv type description', max_length=2000)
    invtyp_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    invtyp_createddate = models.DateTimeField(default=timezone.now)
    invtyp_modifiedby = models.ForeignKey(User, related_name='invtyp_editor', on_delete=models.SET_NULL, null=True)
    invtyp_modifieddate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.invtyp_name

    def get_absolute_url(self):
        return reverse('invtyp-detail', kwargs={"pk": self.pk})


class Invoice(models.Model):
    inv_id = models.AutoField(primary_key=True)
    inv_reference = models.CharField('invoice reference', max_length=50)
    inv_quantity = models.DecimalField('invoice quantity number', max_digits=10, decimal_places=2)
    inv_quantity_type_fk = models.ForeignKey(ChargeUnitType, verbose_name='invoice quantity type', on_delete=models.SET_NULL, null=True)
    inv_cost_value = MoneyField(max_digits=14, decimal_places=2, null=True, default_currency='GBP')
    inv_unit_cost = MoneyField(max_digits=14, decimal_places=2, null=True, default_currency='GBP')
    inv_date = models.DateField(verbose_name='Invoice Date', null=True)
    inv_gr_reference = models.CharField('invoice gr reference', max_length=50, null=True)
    inv_gr_date = models.DateField(verbose_name='gr date', null=True)
    inv_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    inv_createddate = models.DateTimeField(default=timezone.now)
    inv_modifiedby = models.ForeignKey(User, related_name='inv_editor', on_delete=models.SET_NULL, null=True)
    inv_modifieddate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.inv_reference

    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={"pk": self.pk})


class INVNote(models.Model):
    invnote_inv_fk = models.ForeignKey(Invoice, verbose_name='Invoice', on_delete=models.SET_NULL, null=True)
    invnote_note = models.CharField('Invoice Note', max_length=2500)
    invnote_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    invnote_createddate = models.DateTimeField(default=timezone.now)
    invnote_modifiedby = models.ForeignKey(User, related_name='invnote_editor', on_delete=models.SET_NULL, null=True)
    invnote_modifieddate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.invnote_note

    def get_absolute_url(self):
        return reverse('invnote-detail', kwargs={"pk": self.pk})


class INVMatrix(models.Model):
    invmtx_id = models.AutoField(primary_key=True)
    invmtx_inv_id = models.ForeignKey(Invoice, verbose_name='invoice', on_delete=models.SET_NULL, null=True)
    invmtx_po_id = models.ForeignKey(PurchaseOrder, verbose_name='purchase order', on_delete=models.SET_NULL, null=True)
    invmtx_project_fk = models.ForeignKey(Project, verbose_name='project', on_delete=models.SET_NULL, null=True)
    invmtx_customer_fk = models.ForeignKey(Customer, verbose_name="customer", on_delete=models.SET_NULL, null=True)
    invmtx_supplier_fk = models.ForeignKey(Supplier, verbose_name="supplier", on_delete=models.SET_NULL, null=True)
    invmtx_approver_fk = models.ForeignKey(Approver, verbose_name="approver", on_delete=models.SET_NULL, null=True)
    invmtx_apprvd_date = models.DateField(verbose_name='approved date', null=True)
    invmtx_status_fk = models.ForeignKey(INVStatus, verbose_name="inv status", on_delete=models.SET_NULL, null=True)
    invmtx_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    invmtx_createddate = models.DateTimeField(default=timezone.now)
    invmtx_modifiedby = models.ForeignKey(User, related_name='invtx_editor', on_delete=models.SET_NULL, null=True)
    invmtx_modifieddate = models.DateTimeField(auto_now=True, null=True)
