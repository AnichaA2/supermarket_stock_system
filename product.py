# this class shows encapsulation because data and methods are together
class Product:
    def __init__(self, name, price, quantity, category, min_quantity=5):
        #constructor method
        # encapsulation - product data is stored inside the object 
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.min_quantity = min_quantity

    def reduce_stock(self, amount): #reduces product quantity after sale
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Not enough stock available.")

    def increase_stock(self, amount):
        self.quantity += amount

    def is_stock_low(self):
        return self.quantity <= self.min_quantity

    def to_dict(self): #converts object data to dictionary
        # used for saving data to json file
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
            "min_quantity": self.min_quantity
        }

    def __str__(self):
        # returns product info as readable text
        return f"{self.name} | Price: {self.price} | Qty: {self.quantity} | Category: {self.category}"
