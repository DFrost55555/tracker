from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from apps.resources.models import Resource, ResourceType
from apps.items.models import Item, ItemType
from apps.suppliers.models import Supplier
from apps.list.models import POItemType, ChargeUnitType
from django.urls import reverse


class PurchaseOrder(models.Model):
    po_id = models.AutoField(primary_key=True)
    po_reference = models.CharField('po reference', max_length=50)
    po_quantity = models.DecimalField('po quantity number', max_digits=10, decimal_places=2)
    po_quantity_type_fk = models.ForeignKey(ChargeUnitType, verbose_name='po quantity type',on_delete=models.SET_NULL, null=True)
    po_cost_value = models.DecimalField('po cost value', max_digits=10, decimal_places=2)
    po_unit_cost = models.DecimalField('po unit cost', max_digits=10, decimal_places=2)
    po_charge_value = models.DecimalField('po charge value', max_digits=10, decimal_places=2)
    po_unit_charge = models.DecimalField('po unit charge', max_digits=10, decimal_places=2)
    po_start_date = models.DateField(verbose_name='Start Date', null=True)
    po_end_date = models.DateField(verbose_name='End Date', null=True)
    po_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    po_createddate = models.DateTimeField(default=timezone.now)
    po_modifiedby = models.ForeignKey(User, related_name='po_editor',on_delete=models.SET_NULL, null=True)
    po_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.po_reference

    def get_absolute_url(self):
        return reverse ('purorder-detail', kwargs={"pk": self.pk})