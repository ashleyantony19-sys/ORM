from django.db import models
from django.contrib import admin

class CustomerDB(models.Model):
      Customer_Name=models.CharField(max_length=12);
      Order_No=models.IntegerField(primary_key=True);
      Mobile_No=models.IntegerField();
      Address=models.CharField(max_length=100);
      Ratings=models.FloatField();
      Pickup_Time=models.TimeField();
      Order_delivered_time=models.TimeField();

class CustomerDBAdmin(admin.ModelAdmin):
     list_display=['Customer_Name','Order_No','Mobile_No','Address','Ratings','Pickup_Time','Order_delivered_time'];
