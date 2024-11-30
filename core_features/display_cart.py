def display_cart(cart: list):
    if not cart:
        print("\nYour cart 🛒 is empty! 😱")
        return None, 0

    # Display each item in the cart
    print("\nCurrent Cart 🛒:")
    total_cost = 0
    for item in cart:
        ID = item["ID"]
        name = item["name"]
        quantity = item["quantity"]
        price = item["price"]
        item_total = quantity * price
        total_cost += item_total

        print(f"({ID}) - {name}: {quantity} x ₹{price} = ₹{item_total}")
    
    return cart, total_cost
