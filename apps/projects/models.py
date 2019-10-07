from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.customers.models import Customer
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
    project_chargecodetype_fk = models.ForeignKey(ChgCodeType, verbose_name='Charge Code Type', on_delete=models.SET_NULL, null=True)
    project_statustype_fk = models.ForeignKey(StatusType, verbose_name='Status', on_delete=models.SET_NULL, null=True)
    project_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project_createddate = models.DateTimeField(default=timezone.now)
    project_modifiedby = models.ForeignKey(User, related_name='prj_editor',on_delete=models.SET_NULL, null=True)
    project_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse ('project-detail', kwargs={"pk": self.pk})
    
class ProjectResources(models.Model):
    pr_id = models.AutoField(primary_key=True)
    pr_project_fk = models.ForeignKey(Project, verbose_name='project', on_delete=models.SET_NULL, null=True)
    pr_resource_fk = models.ForeignKey(Resource, verbose_name='resource', on_delete=models.SET_NULL, null=True)
    pr_statustype_fk = models.ForeignKey(StatusType, verbose_name='res status', on_delete=models.SET_NULL, null=True)