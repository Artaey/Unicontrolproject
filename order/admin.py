from django.contrib import admin
from .models import SyncSparepart, Price, SyncBomList, DropdownField, DropdownOption, User, UserSave, UserSaveChoise, Order

# Register your models here.
class SyncSparepartAdmin(admin.ModelAdmin):
    list_display = ("no", "name", "itemDescription")
    search_fields = ("name", "itemDescription")
admin.site.register(SyncSparepart, SyncSparepartAdmin)

class PriceAdmin(admin.ModelAdmin):
    list_display = ("no", "priceEUR", "priceDKK", "priceUSD", "priceAUD")
admin.site.register(Price)

class SyncBomListAdmin(admin.ModelAdmin):
     list_display = ("parentItemNo","no", "quantity")
admin.site.register(SyncBomList, SyncBomListAdmin)

class DropdownFieldAdmin(admin.ModelAdmin):
    list_display = ("parentCategory","lableText", "dropdownRequired", "readMore")
admin.site.register(DropdownField, DropdownFieldAdmin)

class DropdownOptionAdmin(admin.ModelAdmin):
    list_display = ("fieldId", "itemNo", "optionText")
admin.site.register(DropdownOption, DropdownOptionAdmin)

admin.site.register(User)

class UserSaveAdmin(admin.ModelAdmin):
    list_display = ("userId", "fieldId", "name", "isFavorite")
admin.site.register(UserSave, UserSaveAdmin)

class UserSaveChoiseAdmin(admin.ModelAdmin):
    list_display = ("saveId", "fieldId", "optionId")
admin.site.register(UserSaveChoise, UserSaveChoiseAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("userId", "itemNo", "orderNumber", "price")
admin.site.register(Order, OrderAdmin)