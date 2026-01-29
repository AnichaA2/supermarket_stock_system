import json
from product import Product

class FileHandler:
    def __init__(self, filename="products.json"):
        self.filename = filename

    def save_products(self, products):
        data = [p.to_dict() for p in products]
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_products(self):
        products = []
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                for item in data:
                    products.append(Product(
                        item["name"],
                        item["price"],
                        item["quantity"],
                        item["category"],
                        item["min_quantity"]
                    ))
        except FileNotFoundError:
            pass

        return products
