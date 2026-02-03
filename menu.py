from stock_manager import StockManager

class Menu:

    @staticmethod
    def start():
        manager = StockManager()

        print("\n--- LOW STOCK ALERTS AT STARTUP ---")
        manager.check_low_stock()

        while True:
            print("\n--- SUPERMARKET STOCK SYSTEM ---")
            print("1. Add product")
            print("2. View products")
            print("3. Check low stock")
            print("4. Sell product")
            print("5. Restock product")
            print("6. Delete product")
            print("7. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Product name: ").strip()
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
                category = input("Category: ")
                manager.add_product(name, price, quantity, category, min_qty)

            elif choice == "2":
                manager.show_products()

            elif choice == "3":
                manager.check_low_stock()

            elif choice == "4":
                name = input("Product name: ")
                qty = input("Quantity to sell: ")
                if not qty.isdigit():
                    print("Invalid quantity.")
                    continue
                qty = int(qty)
                manager.sell_product(name, qty)

            elif choice == "5":
                name = input("Product name: ").strip()
                if name == "" or name.isdigit():
                    print("Product name must contain letters")
                    continue
                qty = input("Quantity to restock: ")
                if not qty.isdigit():
                    print("Invalid quantity.")
                    continue
                qty = int(qty)
                
                manager.restock_product(name, qty)

            elif choice == "6":
                # --- FIXED DELETE OPTION ---
                name = input("Enter product name to delete: ").strip()
                if name == "":
                    print("Name cannot be empty.")
                    continue
                # Assuming your StockManager has a delete_product method
                manager.delete_product(name) 

            elif choice == "7":
                # --- FIXED SYNTAX & INDENTATION ---
                print("Exiting program...")
                break
            
            else:
                print("Invalid option. Please try again.")