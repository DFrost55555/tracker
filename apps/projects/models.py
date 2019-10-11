from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.customers.models import Customer
from apps.resources.models import Resource, ResourceType
from apps.items.models import Item, ItemType
from apps.suppliers.models import Supplier
from apps.roles.models import Role
from apps.statustype.models import StatusType
from apps.chgcodetype.models import ChgCodeType
from apps.lists.models import Location, ProjectStatus, ResourceStatus, ChargeCodeType, ChargeUnitType
from apps.resources.models import Resource
from django.urls import reverse


class Project(models.Model):
    project_name = models.CharField('Project Name', max_length=150)
    project_customer_fk = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.SET_NULL, null=True)
    project_reference = models.CharField('Project Reference', max_length=255)
    project_chargecode = models.CharField('Charge Code',max_length=255)
    project_chargecodetype_fk = models.ForeignKey(ChargeCodeType, verbose_name='Charge Code Type', on_delete=models.SET_NULL, null=True)
    project_statustype_fk = models.ForeignKey(ProjectStatus, verbose_name='Status', on_delete=models.SET_NULL, null=True)
    project_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project_createddate = models.DateTimeField(default=timezone.now)
    project_modifiedby = models.ForeignKey(User, related_name='prj_editor',on_delete=models.SET_NULL, null=True)
    project_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.project_reference

    def get_absolute_url(self):
        return reverse ('project-detail', kwargs={"pk": self.pk})
    
class ProjectResources(models.Model):
    pr_id = models.AutoField(primary_key=True)
    pr_project_fk = models.ForeignKey(Project, verbose_name='project', on_delete=models.SET_NULL, null=True)
    pr_customer_fk = models.ForeignKey(Customer, verbose_name="customer", on_delete=models.SET_NULL, null=True)
    pr_resource_fk = models.ForeignKey(Resource, verbose_name='resource', on_delete=models.SET_NULL, null=True)
    pr_role_fk = models.ForeignKey(Role, verbose_name='resource role', on_delete=models.SET_NULL, null=True)
    pr_statustype_fk = models.ForeignKey(ResourceStatus, verbose_name='resource status', on_delete=models.SET_NULL, null=True)
    pr_supplier_fk = models.ForeignKey(Supplier, verbose_name="supplier", on_delete=models.SET_NULL, null=True)
    pr_location_fk = models.ForeignKey(Location, verbose_name="location", on_delete=models.SET_NULL, null=True)
    pr_chargeunit_fk = models.ForeignKey(ChargeUnitType, verbose_name="charge unit", on_delete=models.SET_NULL, null=True)
    pr_start_date = models.DateField(verbose_name='Start Date', null=True)
    pr_end_date = models.DateField(verbose_name='End Date', null=True)
    pr_cost = models.DecimalField(verbose_name='Cost', max_digits=10, decimal_places=2)
    pr_xcharge = models.DecimalField(verbose_name='XCharge', max_digits=10, decimal_places=2)
    pr_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pr_createddate = models.DateTimeField(default=timezone.now)
    pr_modifiedby = models.ForeignKey(User, related_name='prjres_editor',on_delete=models.SET_NULL, null=True)
    pr_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
class ProjectItems(models.Model):
    pitm_id = models.AutoField(primary_key=True)
    pitm_item_id = models.ForeignKey(Item, verbose_name='Item', on_delete=models.SET_NULL, null=True)
    pitm_project_fk = models.ForeignKey(Project, verbose_name='project', on_delete=models.SET_NULL, null=True)
    pitm_customer_fk = models.ForeignKey(Customer, verbose_name="customer", on_delete=models.SET_NULL, null=True)
    pitm_supplier_fk = models.ForeignKey(Supplier, verbose_name="supplier", on_delete=models.SET_NULL, null=True)
    pitm_location_fk = models.ForeignKey(Location, verbose_name="location", on_delete=models.SET_NULL, null=True)
    pitm_chargeunit_fk = models.ForeignKey(ChargeUnitType, verbose_name="charge unit", on_delete=models.SET_NULL, null=True)
    pitm_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pitm_createddate = models.DateTimeField(default=timezone.now)
    pitm_modifiedby = models.ForeignKey(User, related_name='prjitm_editor',on_delete=models.SET_NULL, null=True)
    pitm_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    
    
    
class ProjectContact(models.Model):
    prjcontact = models.AutoField(primary_key=True)
    prjcontact_customer_fk = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.SET_NULL, null=True)
    prjcontact_firstname = models.CharField('First Name', max_length=150)
    prjcontact_lastname = models.CharField('Last Name', max_length=150)
    prjcontact_role = models.CharField('Role', max_length=150, null=True)
    prjcontact_email = models.EmailField('Email Address', max_length=250)
    prjcontact_telnum = models.CharField('Telephone Number', max_length=150)
    prjcontact_mobnumber = models.CharField('Mobile Number', max_length=150)
    prjcontact_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    prjcontact_createddate = models.DateTimeField(default=timezone.now)
    prjcontact_modifiedby = models.ForeignKey(User, related_name='prjcontact_editor', on_delete=models.SET_NULL, null=True)
    prjcontact_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return '%s %s %s' % (self.prjcontact_lastname, ", ", self.prjcontact_firstname)
    
    def get_absolute_url(self):
        return reverse ('prjcontact-detail', kwargs={"pk": self.pk})
    
    
class ProjectNote(models.Model):
    prjnote_customer_fk = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.SET_NULL, null=True)
    prjnote_note = models.CharField('Note', max_length=2500)
    prjnote_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    prjnote_createddate = models.DateTimeField(default=timezone.now)
    prjnote_modifiedby = models.ForeignKey(User, related_name='prjnote_editor', on_delete=models.SET_NULL, null=True)
    prjnote_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.prjnote_note
    
    
    def get_absolute_url(self):
        return reverse ('prjnote-detail', kwargs={"pk": self.pk})