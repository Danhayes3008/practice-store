from django.shortcuts import get_object_or_404
from stock.models import Stock

def basket_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    
    basket = request.session.get('basket', {})
    
    basket_items = []
    total = 0
    stock_count = 0
    for id, quantity in basket.items():
        stock = get_object_or_404(Stock, pk=id)
        total += quantity * stock.price
        stock_count += quantity
        basket_items.append({'id':id, 'quantity':quantity, 'stock':stock})
        
    return {'basket_items': basket_items, 'total':total, 'stock_count':stock_count}
    
        