from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse

class Customer(models.Model):
    cust_name = models.CharField('Customer Name', max_length=150)
    cust_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cust_createddate = models.DateTimeField(default=timezone.now)
    cust_modifiedby = models.ForeignKey(User, related_name='cust_editor', on_delete=models.SET_NULL, null=True)
    cust_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.cust_name

    def get_absolute_url(self):
        return reverse ('customer-detail', kwargs={"pk": self.pk})
    
    
class CustomerContact(models.Model):
    custcontact_customer_fk = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.SET_NULL, null=True)
    custcontact_firstname = models.CharField('First Name', max_length=150)
    custcontact_lastname = models.CharField('Last Name', max_length=150)
    custcontact_email = models.EmailField('Email Address', max_length=250)
    custcontact_telnum = models.CharField('Telephone Number', max_length=150)
    custcontact_mobnumber = models.CharField('Mobile Number', max_length=150)
    custcontact_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    custcontact_createddate = models.DateTimeField(default=timezone.now)
    custcontact_modifiedby = models.ForeignKey(User, related_name='custcontact_editor', on_delete=models.SET_NULL, null=True)
    custcontact_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.custcontact_email

    def get_absolute_url(self):
        return reverse ('custcontact-detail', kwargs={"pk": self.pk})
    
class CustomerNote(models.Model):
    custnote_customer_fk = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.SET_NULL, null=True)
    custnote_note = models.CharField('Note', max_length=2500)
    custnote_createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    custnote_createddate = models.DateTimeField(default=timezone.now)
    custnote_modifiedby = models.ForeignKey(User, related_name='custnote_editor', on_delete=models.SET_NULL, null=True)
    custnote_modifieddate = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
            return self.custnote_note

    def get_absolute_url(self):
        return reverse ('custnote-detail', kwargs={"pk": self.pk})