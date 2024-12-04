from django.shortcuts import render
from django.http import HttpResponse
from .models import SyncSparepart, DropdownField, DropdownOption

# Create your views here.
def index(request):
    return render(request, "order/index.html")

def excavator(request):
    categories = DropdownField.objects.prefetch_related('dropdownoption_set')
    data = []
    for category in categories:
        options = category.dropdownoption_set.all()
        data.append({
            "category": category,
            "options": options,
        })
    return render(request, "order/excavator.html", {"data": data})

def summary(request):
    return render(request, "order/summary.html")

def confirmation(request):
    return render(request, "order/confirmation.html")
