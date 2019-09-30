from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.customers.models import Customer
from django.urls import reverse


CHARGE_CODE_CHOICES = (
    ('wbs','WBS Code'),
    ('ctr', 'Cost Centre'),
    ('trs','MARS Request')
)

STATUS_CHOICES = (
    ('active','Active'),
    ('inactive','Inactive'),
    ('onhold','On Hold'),
    ('archive','Archive'),
)


class Project(models.Model):
    project_name = models.CharField('Project Name', max_length=150)
    project_customer_fk = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.SET_NULL, null=True)
    project_reference = models.CharField('Project Reference', max_length=255)
    project_chargecode = models.CharField('Charge Code',max_length=255)
    project_chargecodetype = models.CharField('Charge Code Type', max_length=25, choices=CHARGE_CODE_CHOICES, default='wbs')
    project_status = models.CharField('Status', max_length=25, choices=STATUS_CHOICES, default='active')
    project_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project_createddate = models.DateTimeField(default=timezone.now)
    project_modifiedby = models.ForeignKey(User, related_name='prj_editor',on_delete=models.SET_NULL, null=True)
    project_modifieddate = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.project_name
