# SaleTransaction processes product sales (Polymorphism and inheritance)

from transaction import Transaction
# oop: inheritance- saletransaction inherits from transaction
class SaleTransaction(Transaction):
    def process(self):
        #polymorphism- overrides process () from transaction
        #this version reduces stock instead of increasing
        if self.quantity <= self.product.quantity:
            self.product.reduce_stock(self.quantity)
            print(f"Sold {self.quantity} of {self.product.name}")
        else:
            print(f"Not enough stock to sell {self.quantity} of {self.product.name}")
