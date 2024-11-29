# Adds a product to the shopping cart
def add_to_cart(pc: dict, cart: list):
    while True:
        product_name = input("\nEnter the product name to add to the cart and 'exit' when you done: ").strip().lower()
        product_found = False # set as false 
        for id, product in pc.products_catalog.items():
            # product validation 
            if product_name in product["name"].lower():
                product_found = True
                # print the founded product summary
                print(f"\n- Found: {product["name"]} (ID: {id}) \n- Description: {product["description"]} \n- Price: ₹{product["price"]} \n- {"In Stock".upper() if product["stock"] >= 1 else "Out of Stock".upper()}")
                # TODO try:
                # *Only in case product in stock
                if product["stock"] >= 1:
                    quantity = int(input("\nQuantity you want to add: ").strip())
                    # validate the quantity
                    if quantity <= 0:
                        print("\nQuantity must be greater than '0'. Try again")
                        return
                    if quantity > product["stock"]:
                        print(f"\nOnly {product["stock"]} units are available.")
                        return
                    
                    # !Add to cart
                    item = {
                        "ID": id,
                        "name": product["name"],
                        "price": product["price"],
                        "quantity": quantity
                    }
                    cart.append(item)
                    # !Reduce stock
                    product["stock"] -= quantity
                    print(f"\nAdded {quantity} quantity of {product["name"]}{"s" if quantity > 1 else ""} to the cart.")
                    break

                # TODO except ValueError:
                #     print("Invalid Input")
                #     return

        if product_name == 'exit':
            break

        if not product_found:
            print("\nProduct not found. Check the spelling and try again")
        

    # print("\n- Current Cart:")
    # for item in cart:
    #     print(f"- {item['name']}: {item['quantity']} x ₹{item['price']} = ₹{item['quantity'] * item['price']}")

