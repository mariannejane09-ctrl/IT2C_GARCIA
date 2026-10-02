# DISPLAY THE RECEIPT

def display_receipt(orders, subtotal, discount, total):
    print()
    print("+=================================+")
    print("|        SWEET LOOP CAFE          |")
    print("+=================================+")
    print("|             RECEIPT             |")
    print("|---------------------------------|")

    for order in orders:
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