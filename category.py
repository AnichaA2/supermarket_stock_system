# category class, groups products by category

class Category:
    def __init__(self, name):
        self.name = name
        self.products = [] # creates an empty list to store products in the category

    def add_product(self, product):
        self.products.append(product) #this method adds a product to the category

    def show_products(self): #shows all products in the category
        print(f"\n--- Category: {self.name} ---")
        for product in self.products: #this loop goes through each product in the category
            print(product)
