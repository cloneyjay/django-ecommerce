from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_detail(request):
    return render(request, 'cart/detail.html', {})

def cart_add(request, product_id):
    #get the cart present in the session
    cart = Cart(request)
    #test the Post request
    if request.POST.get('action') == 'post':
        #get the product object
        product_id = int(request.POST.get('product_id'))
        #look for the product in the database
        product = get_object_or_404(Product, id=product_id)
        #add the product to the cart/ save to session
        cart.add(product=product)
        
        #get the length of the cart
        cart_length = len(cart)
        #return the response
        # response = JsonResponse({'Product Name': product.name})
        response = JsonResponse({'length': cart_length})
        return response

def cart_remove(request, product_id):
    pass

def cart_update(request, product_id):
    pass
