from django.db import models

# Create your models here.
class SyncSparepart(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    itemDescription = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.no}"

class SyncBomList(models.Model):
    parentItemNo = models.ForeignKey(SyncSparepart, on_delete=models.CASCADE, to_field="no")
    no = models.IntegerField()
    itemDescription = models.CharField(max_length=255)
    quantity = models.SmallIntegerField()

    def __str__(self) -> str:
        return f"{self.no}"

class DropdownField(models.Model):
    lableText = models.CharField(max_length=255)
    dropdownRequired = models.BooleanField()
    readMore = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.lableText

class DropdownOption(models.Model):
    fieldId = models.ForeignKey(DropdownField, on_delete=models.CASCADE)
    itemNo = models.ForeignKey(SyncSparepart, on_delete=models.CASCADE, to_field="no")
    optionText = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.fieldId} + {self.itemNo}"

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class Save(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    fieldId = models.ForeignKey(DropdownField, on_delete=models.DO_NOTHING)
    optionId = models.ForeignKey(DropdownOption, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    isFavorite = models.BooleanField()

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    itemNo =  models.ForeignKey(SyncSparepart, on_delete=models.CASCADE, to_field="no")
    orderNumber = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.orderNumber}"