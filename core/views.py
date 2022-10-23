from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import StockModel
from .forms import  StockForm
from django.contrib.auth.decorators import login_required
# Create your views here.

class Baseview(TemplateView):
    template_name= 'core/base.html'



# 'catigory' , 'item_name', 'qty' , 'in_stock_qty', ' in_stock_by', ' issue_qty' , ' issue_by' , ' issue_to' , ' phone_namber' ,
# ' created_by', ' reorder_level' , ' last_updated' , ' export_to_csv'    
    

def home (request):
    return render(request,'core/home.html')




@login_required
def list_item(request):
    lists = StockModel.objects.all()
    return render(request,'core/list_item.html',{'lists':lists})


@login_required
def add_item(request):
    if request.method == "POST":
        form = StockForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect ('list_item')
    form = StockForm()
    return render(request,'core/add_item.html',{'form':form})    
        