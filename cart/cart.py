

class Cart():
    def __init__(self,request):
        self.session = request.session
        #get the current session key if it exists
        cart = self.session.get('session_key')

        #if the User has no session key, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make the cart is available to all pages
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        #check if the product is already in the cart
        if product_id in self.cart:
            # If the product is already in the cart, do nothing
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        

        #save the cart
        self.session.modified = True

    def __len__(self):
        return len(self.cart)
