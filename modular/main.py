# MAIN PROGRAM

from menu import menu, display_menu
from order import get_order
from calculation import calculate_total
from receipt import display_receipt


# Display menu
display_menu(menu)

# Get customer orders
orders = get_order(menu)

# Calculate total
subtotal, discount, total = calculate_total(orders)

# Display receipt
display_receipt(orders, subtotal, discount, total)