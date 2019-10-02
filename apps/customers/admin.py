from django.contrib import admin
from .models import Customer, CustomerContact, CustomerNote

admin.site.register(Customer)
admin.site.register(CustomerContact)
admin.site.register(CustomerNote)
