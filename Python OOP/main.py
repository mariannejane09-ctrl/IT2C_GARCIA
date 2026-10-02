from cafe import Cafe


# Create Cafe object
cafe = Cafe()

# Display menu
cafe.display_menu()

# Get customer orders
cafe.get_order()

# Calculate total
subtotal, discount, total = cafe.calculate_total()

# Display receipt
cafe.display_receipt(subtotal, discount, total)