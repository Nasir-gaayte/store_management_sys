import imp
from django.contrib import admin
from .models import StockModel
from .forms import  StockForm
# Register your models here.



admin.site.register(StockModel)