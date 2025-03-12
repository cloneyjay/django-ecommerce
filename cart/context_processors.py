from .cart import Cart

#create context processor to make cart available to all templates
def cart(request):
    #return the default data for the cart
    return {'cart': Cart(request)}