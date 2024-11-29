from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "order/index.html")

def excavator(request):
    return render(request, "order/excavator.html")

def summary(request):
    return render(request, "order/summary.html")

def confirmation(request):
    return render(request, "order/confirmation.html")
