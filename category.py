# Category class groups products by category

class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print(f"\n--- Category: {self.name} ---")
        for product in self.products:
            print(product)
