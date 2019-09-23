from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Customer(models.Model):
    cust_name = models.CharField(max_length=150, verbose_name = "Customer Name")
    cust_createdby = models.ForeignKey(User, on_delete=models.CASCADE)
    cust_createddate = models.DateTimeField(default=timezone.now)
    cust_modifiedby = models.ForeignKey(User, related_name='editor',on_delete=models.CASCADE)
    cust_modifieddate = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.cust_name
