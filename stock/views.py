from django.shortcuts import render
from .models import Stock

# Create your views here.
def products(request):
    stock = Stock.objects.all()
    return render(request, 'stock.html', {"stock": stock})

