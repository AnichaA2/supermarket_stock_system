# RestockTransaction increases product stock
# inheritance and polymorphism

from transaction import Transaction
#inheritance, restocktransaction inherits from transaction
class RestockTransaction(Transaction):
    def process(self):
        #polymorphism, this method overrides process () from transaction
        #each transaction has different behaviour
        self.product.increase_stock(self.quantity)
        #prints confirmation message
        print(f"Restocked {self.quantity} units of {self.product.name}")
