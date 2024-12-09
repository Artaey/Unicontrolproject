from django.contrib import admin
from .models import SyncSparepart, Price, SyncBomList, DropdownField, DropdownOption, User, Order, OrderItem

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
    list_display = ("parentCategory","lableText", "dropdownRequired", "readMore", "parentImgUrl")
admin.site.register(DropdownField, DropdownFieldAdmin)

class DropdownOptionAdmin(admin.ModelAdmin):
    list_display = ("fieldId", "itemNo", "optionText")
admin.site.register(DropdownOption, DropdownOptionAdmin)

admin.site.register(User)

admin.site.register(Order)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("orderNumber", "itemNo")
admin.site.register(OrderItem, OrderItemAdmin)