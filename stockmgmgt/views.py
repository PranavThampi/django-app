from typing import ContextManager
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import *
from .forms import StockCreateForm, StockSearchForm

# Create your views here.
def home(request):
    title = 'This is the homepage'
    body = 'This is the body'
    context= {
        'title': title,
        'body': body
    }
    return render(request, "home.html", context)

def list_items(request):
    header = "List of items"
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "header": header,
        "form": form,
        "queryset": queryset,
    }
    if request.method =='POST':
        queryset = Stock.objects.filter(
            category__icontains=form['category'].value(),
            item_name__icontains=form['item_name'].value()
            )
        context = {
            "form": form,
            "header": header,
            "queryset": queryset
        }
    return render(request, "list_items.html", context)

def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_items')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request,"add_items.html",context)
