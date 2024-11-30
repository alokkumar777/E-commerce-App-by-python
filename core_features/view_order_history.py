def view_order_history(order_history: list):
    if not order_history:
        print("\nYou have no order history")
        return

    # print(order_history)

    total_cost = 0
    print("\nYour past orders list 📃")
    for i, item in enumerate(order_history, start=1):
        # ID = item["ID"]
        name = item["name"]
        quantity = item["quantity"]
        price = item["price"]
        item_total = quantity * price
        total_cost += item_total

        print(f"- {i}. {name}: {quantity} x ₹{price} = ₹{item_total}")
    print(f"\nTotal spends ₹{total_cost}")

