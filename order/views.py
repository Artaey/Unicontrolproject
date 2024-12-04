from django.shortcuts import render
from django.http import HttpResponse
from .models import SyncSparepart, Price, DropdownField, DropdownOption

# Front page.
def index(request):
    return render(request, "order/index.html")

# Excavator page
def excavator(request):
    # Step 1: Fetch DropdownFields grouped by parentCategory
    dropdown_fields = DropdownField.objects.prefetch_related('dropdownoption_set')
    
    # Step 2: Prepare a grouped dictionary
    grouped_data = {}
    for field in dropdown_fields:
        category = field.parentCategory or "Uncategorized"
        if category not in grouped_data:
            grouped_data[category] = []
        
        # Step 3: Fetch options for each DropdownField
        options = field.dropdownoption_set.select_related('itemNo')
        
        # Step 4: Attach prices for each option
        options_with_prices = []
        for option in options:
            # Fetch prices via SyncSparepart
            prices = Price.objects.filter(no=option.itemNo).first()
            options_with_prices.append({
                'option': option,
                'prices': {
                    'EUR': prices.priceEUR if prices else None,
                    'DKK': prices.priceDKK if prices else None,
                    'USD': prices.priceUSD if prices else None,
                    'AUD': prices.priceAUD if prices else None,
                }
            })
        
        # Add field and its options with prices to the group
        grouped_data[category].append({
            'field': field,
            'options': options_with_prices
        })
    return render(request, "order/excavator.html", {'grouped_data': grouped_data})

def summary(request):
    return render(request, "order/summary.html")

def confirmation(request):
    return render(request, "order/confirmation.html")
