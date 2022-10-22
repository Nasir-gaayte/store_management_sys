import imp
from django.contrib import admin
from .models import StockModel
from .forms import  StockAddForm, StockForm
# Register your models here.

class StockCreateAdmin(admin.ModelAdmin):
    list_display= ['category','item_name', 'qty']
    form= StockForm
    list_filter= ['category']
    search_fields= ['category', 'item_name']


admin.site.register(StockModel, StockCreateAdmin)