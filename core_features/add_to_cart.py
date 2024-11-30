# Adds a product to the shopping cart
def add_to_cart(pc: dict, cart: list):
    while True:
        product_name = input("\nEnter the product name to add to the cart and 'exit' when you done: ").strip().lower()
        if product_name == 'exit':
            break
        
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
                    
                    # Check if the product is already in the cart
                    product_in_cart = next((item for item in cart if item["ID"] == id), None)
                    # --------------------------------------
                    # product_in_cart = None
                    # for item in cart:
                    #     if item["ID"] == id:
                    #         product_in_cart = item
                    #         break
                    # --------------------------------------
                    if product_in_cart:
                        # Update the quantity of the existing product
                        product_in_cart["quantity"] += quantity
                        print(f"\nUpdated the quantity of {product['name']} to {product_in_cart['quantity']}.")
                    else:
                        # Add new item to the cart
                        item = {
                            "ID": id,
                            "name": product["name"],
                            "price": product["price"],
                            "quantity": quantity,
                        }
                        cart.append(item)
                        print(f"\nAdded {quantity} quantity of {product["name"]}{"s" if quantity > 1 else ""} to the cart.")
                        
                    # !Reduce stock
                    product["stock"] -= quantity
                    break

                # TODO except ValueError:
                #     print("Invalid Input")
                #     return


        if not product_found:
            print("\nProduct not found. Check the spelling and try again")
        

    # print("\n- Current Cart:")
    # for item in cart:
    #     print(f"- {item['name']}: {item['quantity']} x ₹{item['price']} = ₹{item['quantity'] * item['price']}")

