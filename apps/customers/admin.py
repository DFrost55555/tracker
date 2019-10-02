from django.contrib import admin
from .models import Customer, CustomerContact, CustomerNote


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('custcontact_firstname', 'custcontact_lastname','custcontact_role','custcontact_mobnumber','custcontact_email')


admin.site.register(Customer, CustomerAdmin)