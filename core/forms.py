from unittest import mock
from django import forms
from .models import StockModel


class StockForm(forms.ModelForm):
    class Meta:
        model = StockModel
        fields = ['category', 'item_name', 'qty'] 
        
        
        
class StockAddForm(forms.ModelForm):
    class Meta:
        model = StockModel
        exclude = [ 'catigory' , 'item_name', 'qty' , 'in_stock_qty', ' in_stock_by', ' issue_qty' , ' issue_by' , ' issue_to' , ' phone_namber' ,
' created_by', ' reorder_level' ,  ' export_to_csv'    ]        
        