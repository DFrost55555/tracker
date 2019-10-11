from django.contrib import admin
from .models import Item, ItemType


class ItemAdmin(admin.ModelAdmin):
    list_display = ('itm_name', 'itm_item_type_fk')
    list_per_page = 20
    ordering = ('itm_name',)

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType)
