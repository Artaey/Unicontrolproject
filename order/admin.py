from django.contrib import admin
from .models import SyncSparepart, SyncBomList, DropdownField, DropdownOption, User, Save, Order

# Register your models here.
class SyncSparepartAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'itemDescription', 'price') 
    search_fields = ('name', 'itemDescription')
admin.site.register(SyncSparepart, SyncSparepartAdmin)

class SyncBomListAdmin(admin.ModelAdmin):
    list_display = ('no', 'itemDescription', 'quantity', 'parentItemNo')
admin.site.register(SyncBomList, SyncBomListAdmin)

class DropdownFieldAdmin(admin.ModelAdmin):
    list_display = ('lableText', 'dropdownRequired', 'readMore')
admin.site.register(DropdownField, DropdownFieldAdmin)

class DropdownOptionAdmin(admin.ModelAdmin):
    list_display = ('fieldId', 'itemNo', 'optionText')
admin.site.register(DropdownOption, DropdownOptionAdmin)

admin.site.register(User)

class SaveAdmin(admin.ModelAdmin):
    list_display = ('userId', 'fieldId', 'optionId', 'name', 'isFavorite')
admin.site.register(Save, SaveAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('userId', 'itemNo', 'orderNumber', 'price')
admin.site.register(Order, OrderAdmin)