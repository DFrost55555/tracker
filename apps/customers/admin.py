from django.contrib import admin
from .models import Customer, CustomerContact, CustomerNote

admin.site.register(Customer)
admin.site.register(CustomerContact)
admin.site.register(CustomerNote)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('custcontact_firstname', 'custcontact_lastname','custcontact_role','custcontact_mobnumber','custcontact_email')
    