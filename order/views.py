from django.shortcuts import render
from django.http import HttpResponse
from .models import SyncSparepart, Price, DropdownField, DropdownOption

# Front page.
def index(request):
    return render(request, "order/index.html")

# Excavator page
def excavator(request):
    dropdown_fields = DropdownField.objects.prefetch_related("dropdownoption_set")
    
    grouped_data = {}
    for field in dropdown_fields:
        category = field.parentCategory or "Uncategorized"
        if category not in grouped_data:
            grouped_data[category] = []
        
        options = field.dropdownoption_set.select_related("itemNo")
        
        options_with_prices = []
        for option in options:
            prices = Price.objects.filter(no=option.itemNo).first()
            options_with_prices.append({
                "option": option,
                "prices": {
                    "EUR": prices.priceEUR if prices else None,
                }
            })

        grouped_data[category].append({
            "field": field,
            "isRequired": field.dropdownRequired,
            "readMore": field.readMore,
            "options": options_with_prices,
        })
    return render(request, "order/excavator.html", {"grouped_data": grouped_data})

def summary(request):
    return render(request, "order/summary.html")

def confirmation(request):
    return render(request, "order/confirmation.html")
