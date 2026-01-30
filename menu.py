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
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Product name: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                category = input("Category: ")
                min_qty = int(input("Minimum quantity: "))
                manager.add_product(name, price, quantity, category, min_qty)

            elif choice == "2":
                manager.show_products()

            elif choice == "3":
                manager.check_low_stock()

            elif choice == "4":
                name = input("Product name: ")
                qty = int(input("Quantity to sell: "))
                manager.sell_product(name, qty)

            elif choice == "5":
                name = input("Product name: ")
                qty = int(input("Quantity to restock: "))
                manager.restock_product(name, qty)

            elif choice == "6":
                print("Exiting program...")
                break

            else:
                print("Invalid option.")
