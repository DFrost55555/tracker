from django.contrib import admin
from .models import Customer, CustomerContact, CustomerNote


class CustomerContactAdmin(admin.ModelAdmin):
    list_display = ('custcontact_firstname', 'custcontact_lastname','custcontact_role','custcontact_mobnumber','custcontact_email')
    list_display_links = ('custcontact_firstname', 'custcontact_lastname')
    list_per_page = 15

admin.site.register(Customer)
admin.site.register(CustomerContact, CustomerContactAdmin)
admin.site.register(CustomerNote)