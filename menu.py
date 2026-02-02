from stock_manager import StockManager

class Menu:

    @staticmethod # used to start the menu without creating an object
    def start(): # abstraction, menu hides how system works internally
        manager = StockManager() # creates the main controller object

        print("\n--- LOW STOCK ALERTS AT STARTUP ---")
        manager.check_low_stock()

        while True: #keeps the menu running
            print("\n--- SUPERMARKET STOCK SYSTEM ---")
            print("1. Add product")
            print("2. View products")
            print("3. Check low stock")
            print("4. Sell product")
            print("5. Restock product")
            print("6. Exit") # displays menu options

            choice = input("Choose an option: ") # gets the user input

            if choice == "1": # user wants to add a product
                name = input("Product name: "). strip()
                if name == "" or name.isdigit():
                    print("Invalid product name.")
                    continue
                try:
                    price = float(input("Price: "))
                    quantity = int(input("Quantity: "))
                    min_qty = int(input("Minimum quantity: "))
                except ValueError:
                    print("Invalid number input.")
                    continue
                category: str = input("Category: ")
                manager.add_product(name, price, quantity, category, min_qty) # delegates logic to stock manager

            elif choice == "2": #shows all products
                manager.show_products()

            elif choice == "3": #checks low stock
                manager.check_low_stock()

            elif choice == "4":
                name = input("Product name: ")
                qty = input("Quantity to sell: ")
                if not qty.isdigit():
                    print("Invalid quantity.")
                    continue
                manager.sell_product(name, qty) #sale logic handled by stockmanager

            elif choice == "5":
                name = input("Product name: "). strip()

                if name == "" or name.isdigit():
                    print("Product name must contain letters"); continue

                qty = input ("Quantity to restock: ")

                if not qty.isdigit():
                    print("Invalid quantity.")
                    continue
                manager.restock_product(name, qty) #restock logic handled by stockmanager

            elif choice == "6":
                print("Exiting program...")
                break # ends the program

            else:
                print("Invalid option.") # handles wrong input
