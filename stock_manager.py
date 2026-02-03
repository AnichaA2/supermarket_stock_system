# StockManager controls the system logic, because all stock operations are handled inside this class

from file_handler import FileHandler
from category import Category
from sale_transaction import SaleTransaction
from restock_transaction import RestockTransaction
from product import Product

class StockManager:
    def __init__(self):
        #encapsulation: internal system data
        self.file_handler = FileHandler()
        self.products = self.file_handler.load_products()
        self.categories = {}

        for product in self.products: # add loaded products into categories
            self.add_to_category(product)

    def add_to_category(self, product):
        if product.category not in self.categories:
            self.categories[product.category] = Category(product.category)
        self.categories[product.category].add_product(product)

    def add_product(self, name, price, quantity, category, min_quantity):
        product = Product(name, price, quantity, category, min_quantity)
        self.products.append(product)
        self.add_to_category(product)
        self.file_handler.save_products(self.products)
        print("Product added successfully.")

    def show_products(self):
        if not self.products:
            print("No products available.")
            return
        for product in self.products:
            print(product)

    def check_low_stock(self):
        low_found = False
        for product in self.products:
            if product.is_stock_low():
                print(f"ALERT: {product.name} stock is low ({product.quantity})")
                low_found = True
        if not low_found:
            print("Stock level is sufficient.")

    def find_product_by_name(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def sell_product(self, product_name, quantity):
        product = self.find_product_by_name(product_name)
        if product:
            transaction = SaleTransaction(product, quantity)
            transaction.process()
            self.file_handler.save_products(self.products)
        else:
            print("Product not found.")

    def restock_product(self, product_name, quantity):
        product = self.find_product_by_name(product_name)
        if product:
            #abstraction
            transaction = RestockTransaction(product, quantity)
            transaction.process() #polymorphism here
            self.file_handler.save_products(self.products)
        else:
            print("Product not found.")
            def delete_product(self, product_name):
                product = self.find_product_byname(product_name)

                if product:
                    self.products.remove(product)
                    self.file_handler.save_products(self.products)
                    print("product deleted.")
                else:
                    print("product not found.")

    