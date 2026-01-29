# SaleTransaction processes product sales (Polymorphism)

from transaction import Transaction

class SaleTransaction(Transaction):
    def process(self):
        if self.quantity <= self.product.quantity:
            self.product.reduce_stock(self.quantity)
            print(f"Sold {self.quantity} of {self.product.name}")
        else:
            print(f"Not enough stock to sell {self.quantity} of {self.product.name}")
