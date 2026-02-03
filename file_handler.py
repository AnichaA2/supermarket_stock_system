import json # used to work with json files
from product import Product # used to recreate product objects from file

class FileHandler:
    def __init__(self): #oop: encapsulation, file name belongs to this object only
        filename="products.json"
        self.filename = filename # store the file name

    def save_products(self, products): # abstraction, other classes do not know how saving works
        data = [p.to_dict() for p in products] #convert objects to dictionaries
        with open(self.filename, "w") as file: 
            json.dump(data, file, indent=4) # save data to json file

    def load_products(self): #abstraction, hides file reading logic from the system
        products = [] #list to store loaded products
        try:
            with open(self.filename, "r") as file:
                data = json.load(file) # read json data
                for item in data:
                    products.append(Product(
                        item["name"],
                        item["price"],
                        item["quantity"],
                        item["category"],
                        item["min_quantity"]
                    )) # create product objects
        except FileNotFoundError:
            pass # ignore if file does not exist

        return products # return product list
