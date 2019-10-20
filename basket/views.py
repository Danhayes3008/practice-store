from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_basket(request):
    return render(request, 'basket.html')
    
def add_to_basket(request, id):
    quantity = int(request.POST.get('quantity'))
    
    basket = request.session.get('basket', {})
    if id in basket:
        basket[id] = int(basket[id]) + quantity
    else:
        basket[id] = basket.get(id, quantity)
        
    request.session['basket'] = basket
    return redirect(reverse('index'))
    
def adjust_basket(request, id):
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    
    if quantity > 0:
        basket[id] = quantity
    else:
        basket.pop(id)
        
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))