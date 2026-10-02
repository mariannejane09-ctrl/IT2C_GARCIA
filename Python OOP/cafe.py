class Cafe:

    def __init__(self):
        self.menu = {
            1: ("Glazed Donut", 45),
            2: ("Chocolate Donut", 55),
            3: ("Strawberry Donut", 60),
            4: ("Boston Cream", 70),
            5: ("Americano", 90),
            6: ("Latte", 120),
            7: ("Cappuccino", 130),
            8: ("Mocha", 140),
            9: ("Croissant", 80),
            10: ("Cinnamon Roll", 95)
        }

        self.orders = []


    # DISPLAY MENU
    def display_menu(self):
        print("+=================================+")
        print("|        SWEET LOOP CAFE          |")
        print("+=================================+")
        print("|              MENU               |")
        print("|---------------------------------|")
        print("| DONUTS                          |")
        print("| [1] Glazed Donut            ₱45 |")
        print("| [2] Chocolate Donut         ₱55 |")
        print("| [3] Strawberry Donut        ₱60 |")
        print("| [4] Boston Cream            ₱70 |")
        print("|---------------------------------|")
        print("| COFFEE                          |")
        print("| [5] Americano               ₱90 |")
        print("| [6] Latte                  ₱120 |")
        print("| [7] Cappuccino             ₱130 |")
        print("| [8] Mocha                  ₱140 |")
        print("|---------------------------------|")
        print("| PASTRIES                        |")
        print("| [9] Croissant               ₱80 |")
        print("| [10] Cinnamon Roll          ₱95 |")
        print("+=================================+")


    # GET CUSTOMER ORDER
    def get_order(self):
        while True:
            try:
                choice = int(input("Enter choice: "))

                if choice not in self.menu:
                    print("Invalid choice! Please choose from the menu.")
                    continue

                quantity = int(input("Enter Quantity: "))

                if quantity <= 0:
                    print("Quantity must be at least 1.")
                    continue

                item_name = self.menu[choice][0]
                item_price = self.menu[choice][1]

                self.orders.append([item_name, quantity, item_price])

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


    # CALCULATE TOTAL
    def calculate_total(self):
        subtotal = 0

        for order in self.orders:
            item_quantity = order[1]
            item_price = order[2]

            item_total = item_quantity * item_price
            subtotal += item_total

        if subtotal >= 500:
            discount = subtotal * 0.10
        else:
            discount = 0

        total = subtotal - discount

        return subtotal, discount, total


    # DISPLAY RECEIPT
    def display_receipt(self, subtotal, discount, total):
        print()
        print("+=================================+")
        print("|        SWEET LOOP CAFE          |")
        print("+=================================+")
        print("|             RECEIPT             |")
        print("|---------------------------------|")

        for order in self.orders:
            item_name = order[0]
            quantity = order[1]
            price = order[2]
            item_total = quantity * price

            print(f"{item_name:<20}")
            print(f"{quantity} x ₱{price:<6} = ₱{item_total:<6}")

        print("-----------------------------------")
        print(f"SUBTOTAL:                 ₱{subtotal:>6.2f}")
        print(f"DISCOUNT:                -₱{discount:>6.2f}")
        print(f"TOTAL:                    ₱{total:>6.2f}")
        print("+=================================+")
        print("|      THANK YOU! COME AGAIN!     |")
        print("+=================================+")