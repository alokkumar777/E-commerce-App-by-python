def view_order_history(past_order: list):
    if not past_order:
        print("\nYou ordered nothing yet")
        return

    # print(past_order)

    total_cost = 0
    print("\nYour past orders list 📃")
    for i, item in enumerate(past_order, start=1):
        # ID = item["ID"]
        name = item["name"]
        quantity = item["quantity"]
        price = item["price"]
        item_total = quantity * price
        total_cost += item_total

        print(f"- {i}. {name}: {quantity} x ₹{price} = ₹{item_total}")
    print(f"\nTotal spends ₹{total_cost}")

