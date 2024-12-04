from django.db import models

# Create your models here.
class SyncSparepart(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    itemDescription = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.no}"
    
class Price(models.Model):
    no = models.ForeignKey(SyncSparepart, on_delete=models.CASCADE, to_field="no")
    priceEUR = models.IntegerField()
    priceDKK = models.IntegerField()
    priceUSD = models.IntegerField()
    priceAUD = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.no}"

class SyncBomList(models.Model):
    parentItemNo = models.ForeignKey(
        SyncSparepart,
        on_delete=models.CASCADE,
        to_field="no",
        related_name="bom_parent_item",
    )
    no = models.ForeignKey(
        SyncSparepart,
        on_delete=models.CASCADE,
        to_field="no",
        related_name="bom_clild_item",
    )
    quantity = models.SmallIntegerField()

    def __str__(self) -> str:
        return f"{self.no}"

class DropdownField(models.Model):
    parentCategory = models.CharField(max_length=100, default=None, blank=True, null=True)
    lableText = models.CharField(max_length=50)
    dropdownRequired = models.BooleanField()
    readMore = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.lableText

class DropdownOption(models.Model):
    fieldId = models.ForeignKey(DropdownField, on_delete=models.CASCADE)
    itemNo = models.ForeignKey(SyncSparepart, on_delete=models.CASCADE, to_field="no")
    optionText = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.fieldId} + {self.itemNo}"

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class UserSave(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    fieldId = models.ForeignKey(DropdownField, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    isFavorite = models.BooleanField()

    def __str__(self) -> str:
        return self.name
    
class UserSaveChoise(models.Model):
    saveId = models.ForeignKey(UserSave, on_delete=models.CASCADE)
    fieldId = models.ForeignKey(DropdownField, on_delete=models.DO_NOTHING)
    optionId = models.ForeignKey(DropdownOption, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.saveId
    
class Order(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    itemNo =  models.ForeignKey(SyncSparepart, on_delete=models.CASCADE, to_field="no")
    orderNumber = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.orderNumber}"