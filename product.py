class Product:
    def __init__(self, name, price, quantity, category, min_quantity=5):
        # ENCAPSULATION: Double underscores (__) make these attributes PRIVATE
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__category = category
        self.__min_quantity = min_quantity

  # --- GETTERS: These allow other files to READ private data ---
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def category(self):  # <--- ADICIONE ESTE AQUI
        return self.__category

    # --- METHODS: The only way to MODIFY the data ---
    def reduce_stock(self, amount): 
        if amount <= self.__quantity:
            self.__quantity -= amount
        else:
            print("Not enough stock available.")

    def increase_stock(self, amount):
        self.__quantity += amount

    def is_stock_low(self):
        return self.__quantity <= self.__min_quantity

    def to_dict(self): 
        return {
            "name": self.__name,
            "price": self.__price,
            "quantity": self.__quantity,
            "category": self.__category,
            "min_quantity": self.__min_quantity
        }

    def __str__(self):
        return f"{self.__name} | Price: {self.__price} | Qty: {self.__quantity} | Category: {self.__category}"