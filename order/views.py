from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import SyncSparepart, SyncBomList, Price, DropdownField, Order, OrderItem

# Front page.
def index(request):
    return render(request, "order/index.html")

# Excavator page
def excavator(request):
    dropdown_fields = DropdownField.objects.filter(parentCategory__isnull=False).prefetch_related("dropdownoption_set").order_by("-dropdownRequired")
    
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
            "parentImgUrl": field.parentImgUrl,
            "readMore": field.readMore,
            "options": options_with_prices,
        })
    return render(request, "order/excavator.html", {"grouped_data": grouped_data})

def summary(request):
    if request.method == "POST":

        received_data = request.POST.dict()

        print("Received data:", received_data)

        last_order = Order.objects.order_by('-orderNumber').first()
        next_order_number = last_order.orderNumber + 1 if last_order else 1

        new_order = Order.objects.create(orderNumber=next_order_number)

        for key, item_no in received_data.items():
            try:
                sparepart = SyncSparepart.objects.get(no=item_no)

                OrderItem.objects.create(orderNumber=new_order, itemNo=sparepart)

            except SyncSparepart.DoesNotExist:
                print(f"ItemNo {item_no} does not exist in SyncSparepart.")

        return JsonResponse({
            "message": "Order created successfully",
            "orderNumber": new_order.orderNumber,
            "data": received_data
        })

    return render(request, "order/summary.html")

def getCartItems(request):
    if request.method == "POST":

        item_ids = request.POST.getlist("item_ids[]", [])
        items = []

        for item_id in item_ids:
            try:
                sparepart = SyncSparepart.objects.get(no=item_id)
                price = Price.objects.get(no=sparepart)
                isKit = "SparepartKit" in sparepart.name

                items.append({
                    "id": sparepart.no,
                    "description": sparepart.itemDescription,
                    "netPrice": price.priceEUR,
                    "msrp": round(price.priceEUR * 1.4),
                    "isKit": isKit,
                    "isParent": True,
                    "isChild": False,
                })
                
                if isKit:
                    child_items = SyncBomList.objects.filter(parentItemNo=sparepart)
                    for child in child_items:
                        try:
                            child_sparepart = child.no

                            child_price = Price.objects.get(no=child_sparepart)

                            items.append({
                                "id": child_sparepart.no,
                                "description": child_sparepart.itemDescription,
                                "netPrice": child_price.priceEUR,
                                "msrp": round(child_price.priceEUR * 1.4),
                                "quantity": child.quantity,
                                "isKit": False, 
                                "isParent": False,
                                "isChild": True,
                            })
                        except Exception as e:
                            print(f"Error processing child item: {e}")

            except (SyncSparepart.DoesNotExist, Price.DoesNotExist):
                continue

        return JsonResponse({"items": items}, status=200)

    return JsonResponse({"error": "Invalid request"}, status=400)
