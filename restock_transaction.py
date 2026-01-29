# RestockTransaction increases product stock (Polymorphism)

from transaction import Transaction

class RestockTransaction(Transaction):
    def process(self):
        self.product.increase_stock(self.quantity)
        print(f"Restocked {self.quantity} units of {self.product.name}")
