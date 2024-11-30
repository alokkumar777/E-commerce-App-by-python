import time
def place_order(dc, cart: list, past_order: list):
    # Use display_cart to show cart details
    cart_data, total_cost = dc.display_cart(cart)
    if cart_data is None:
        return None
    print(f"\n💵 Total cost: ₹{total_cost}")
    confirm = input("\nDo you want to place order? (y/n): ").strip().lower()
    if confirm == 'y':
        # payment processing
        print("\nChoose a payment method: \n1. Pay on Delivery \n2. UPI")

        while True:
            choice = input("Enter your choice (1 or 2): ").strip()
            if choice == '1':
                payment_method = "Pay on Delivery"
                print("\nKeep the exact amount ready")
                break
            elif choice == '2':
                payment_method = "UPI"
                upi_id = input("\nEnter your UPI: ").strip()
                # payment process
                print(f"\nUPI payment initiated. Using UPI ID: {upi_id}")
                # print("\nProcessing payment... Please wait.")
                # countdown 
                for timer in range(6, 0, -1):
                    print(f"⌛ Processing payment... Please wait {timer} seconds remaining...", end="\r", flush=True)
                    time.sleep(1)
                # clear countdown msg
                print(" " * 60, end="\r") # overwrite
                print("\n✅ Payment Successful!")
                break
            else:
                print("\nInvalid choice. Please enter 1 or 2")
        
        # display order summary
        print("Order Summary:")
        for item in cart:
            ID = item["ID"]
            name = item["name"]
            quantity = item["quantity"]
            price = item["price"]
            print(f"- {name}, Qty{quantity} - ₹{price}")
        # print(cart_data)
        print(f"💵 Total Paid: ₹{total_cost}")
        print(f"Payment Method: {payment_method}")
        print(f"✅ Order Placed Successful! 🎉")

        past_order.extend(cart_data)
        # clear cart after order placed
        cart.clear()
        # return {
        #     "order_details": cart_data,
        #     "total_cost": total_cost,
        #     "payment_method": payment_method
        # }

    elif confirm == 'n':
        print("\nOrder placement cancelled.")   
    else:
        print("Invalid input!")         

