# Remove from the cart
def remove_from_cart(pc: dict, cart: list):
    while True:
        if not cart:
            print("\nYour cart 🛒 is empty! 👍, There is nothing to remove.")
            return

        print("\n- Current Cart 🛒: ")
        # show the list of item in the cart
        # item is like {"ID": "GXX1", "name": "Rice", "price": 345, "quantity": 4}
        for i, item in enumerate(cart, start=1):
            print(f"\n{i}. ({item["ID"]}) - {item["name"]} -- {item["quantity"]} x ₹{item["price"]} = ₹{item["quantity"] * item["price"]}")
        # asking for 'id' or 'name' of product that user want to remove form the cart
        product_name_or_id = input("\nEnter product name or ID to remove or (type 'exit' to cancel): ").strip().lower()

        if product_name_or_id == 'exit':
            print("\nEXTING... from cart")
            break

        # check product in cart or not
        product_found = False # set to false
        for item in cart:
            if product_name_or_id == item["name"].lower() or product_name_or_id == item["ID"]:
                product_found = True
                #  confirmation msg ALERT!!
                confirm = input(f"\nAre you sure? 🥺 u want to remove {item["name"]} from the cart? (y/n): ").lower()

                if confirm == 'y' or 'yes':
                    pc.products_catalog[item["ID"]]["stock"] += item["quantity"]

                    # remove from the cart
                    cart.remove(item)
                    print(f"\n{item["name"]} has removed from the cart 😭.")
                else:
                    print(f"\nCancelled removal of {item["name"]} 🥰")
                break
        # in case enter product is not the cart
        if not product_found:
            print("\nProduct not found in the cart 🛒")

    