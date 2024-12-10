from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("excavator", views.excavator, name="excavator"),
    path("summary", views.summary, name="summary"),
    path("getCartItems", views.getCartItems, name="getCartItems")
]