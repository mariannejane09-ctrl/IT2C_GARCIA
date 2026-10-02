# GET CUSTOMER ORDER

def get_order(menu):
    orders = []

    while True:
        try:
            choice = int(input("Enter choice: "))

            if choice not in menu:
                print("Invalid choice! Please choose from the menu.")
                continue

            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Quantity must be at least 1.")
                continue

            item_name = menu[choice][0]
            item_price = menu[choice][1]

            orders.append([item_name, quantity, item_price])

            print(f"{quantity} x {item_name} added to your order.")

            another = input(
                "Do you want to order another item? (Y/N): "
            ).upper()

            if another == "N":
                break

            while another != "Y":
                print("Invalid input! Please enter Y or N.")
                another = input(
                    "Do you want to order another item? (Y/N): "
                ).upper()

        except ValueError:
            print("Invalid input! Please enter a number.")

    return orders