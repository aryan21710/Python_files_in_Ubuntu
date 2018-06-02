
class ShoppingCart(object):

    cart={}
    totalPrice=0
    def __init__(self,storeName,addr):
        self.storeName=storeName
        self.addr=addr
        print ('THE NAME OF THE STORE:-',self.storeName)
        print ('THE ADDRESS OF THE STORE:-',self.addr)

    def addItems(self,product,quantity,price):
        self.product=product
        self.quantity=quantity
        self.price=price

        if self.product not in self.cart:
            print ('PRODUCT "{}" ADDED IN THE CART\n'.format(self.product.upper()))
            self.price=self.quantity * self.price
            self.totalPrice+=self.price
            self.cart[product]=self.quantity
        else:
            print ('"{}" PACKETS OF "{}" ALREADY PRESENT IN THE CART. IGNORING IT \n'.\
                   format(self.quantity,self.product.upper()))




lulu=ShoppingCart('lulu SuperMarket','PT Budigere')
lulu.addItems('sugar',2,40)
lulu.addItems('salt',3,10)
lulu.addItems('sugar',4,40)
print ('UPDATED CART IS:- {} \n'.format(lulu.cart))
print ('TOTAL MONEY BILLED IS:- {} \n'.format(lulu.totalPrice))



