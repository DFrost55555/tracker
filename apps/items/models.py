from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class ItemType(models.Model):
    itmtype_id = models.AutoField(primary_key=True)
    itmtype_name = models.CharField('resource type', max_length=100)
    itmtype_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    itmtype_createddate = models.DateTimeField(default=timezone.now)
    itmtype_modifiedby = models.ForeignKey(User, related_name='itmtype_editor',on_delete=models.SET_NULL, null=True)
    itmtype_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.itmtype_name

    def get_absolute_url(self):
        return reverse ('itemtype-detail', kwargs={"pk": self.pk})
    

class Item(models.Model):
    itm_id = models.AutoField(primary_key=True)
    itm_name = models.CharField('item name', max_length=100)
    itm_description = models.CharField('item description', max_length=2000, null=True)
    itm_item_type_fk = models.ForeignKey(ItemType, verbose_name='item type', on_delete=models.SET_NULL, null=True)
    itm_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    itm_createddate = models.DateTimeField(default=timezone.now)
    itm_modifiedby = models.ForeignKey(User, related_name='itm_editor',on_delete=models.SET_NULL, null=True)
    itm_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.itm_name

    def get_absolute_url(self):
        return reverse ('item-detail', kwargs={"pk": self.pk})
