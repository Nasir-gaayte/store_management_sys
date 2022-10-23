from django.db import models

# Create your models here.


class StockModel(models.Model):
    
    category= models.CharField(max_length=50, blank=True, null=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)  
    qty =models.IntegerField(default='0', blank=True, null=True)
    in_stock_qty= models.IntegerField(default="0", blank=True, null=True)
    in_stock_by = models.CharField(max_length=50,blank=True, null=True)
    issue_qty = models.IntegerField(default='0',blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_namber= models.CharField(max_length=50, blank=True, null=True)
    created_by= models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    export_to_csv = models.BooleanField(default=False)
    
# 'catigory' , 'item_name', 'qty' , 'in_stock_qty', ' in_stock_by', ' issue_qty' , ' issue_by' , ' issue_to' , ' phone_namber' ,
# ' created_by', ' reorder_level' , ' export_to_csv'    
    
    
    def __str__(self):
        return f"{self.category} it is in stock from {self.last_updated}"