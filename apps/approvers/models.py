from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Approver(models.Model):
    appr_id = models.AutoField(primary_key=True)
    appr_firstname = models.CharField('firstname', max_length=100)
    appr_lastname = models.CharField('lastname', max_length=100)
    appr_role = models.CharField('role', max_length=150, null=True)
    appr_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    appr_createddate = models.DateTimeField(default=timezone.now)
    appr_modifiedby = models.ForeignKey(User, related_name='appr_editor',on_delete=models.SET_NULL, null=True)
    appr_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return '%s %s %s' % (self.appr_lastname, ", ", self.appr_firstname)

    def get_absolute_url(self):
        return reverse ('approver-detail', kwargs={"pk": self.pk})
