# CALCULATE TOTAL
# DISCOUNT WILL APPLY IF ORDER IS >= 500
# 10% DISCOUNT

def calculate_total(orders):
    subtotal = 0

    for order in orders:
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