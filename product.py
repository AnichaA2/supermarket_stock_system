# Product class represents a product in the supermarket

class Product:
    def __init__(self, name, price, quantity, category, min_quantity=5):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.min_quantity = min_quantity

    def reduce_stock(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Not enough stock available.")

    def increase_stock(self, amount):
        self.quantity += amount

    def is_stock_low(self):
        return self.quantity <= self.min_quantity

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
            "min_quantity": self.min_quantity
        }

    def __str__(self):
        return f"{self.name} | Price: {self.price} | Qty: {self.quantity} | Category: {self.category}"
