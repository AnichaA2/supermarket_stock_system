from stock_manager import StockManager

def main():
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

            # Validate product name
            while True:
                name = input("Product name: ").strip()

                if name == "":
                    print("Product name cannot be empty.")
                    continue

                if len(name) < 2:
                    print("Product name must have at least 2 characters.")
                    continue

                if name.isdigit():
                    print("Product name cannot be numbers.")
                    continue

                break

            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            category = input("Category: ")
            min_quantity = int(input("Minimum quantity: "))

            manager.add_product(name, price, quantity, category, min_quantity)

        elif choice == "2":
            manager.show_products()

        elif choice == "3":
            manager.check_low_stock()

        elif choice == "4":
            product_name = input("Enter product name to sell: ")
            qty = int(input("Enter quantity to sell: "))
            manager.sell_product(product_name, qty)
            manager.check_low_stock()

        elif choice == "5":
            product_name = input("Enter product name to restock: ")
            qty = int(input("Enter quantity to add: "))
            manager.restock_product(product_name, qty)

        elif choice == "6":
            product_name = input("Enter product name to delete: ")
            manager.delete_product(product_name)

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please try again.")

main()
