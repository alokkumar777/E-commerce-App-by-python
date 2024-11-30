def view_cart(dc, cart: list):
    cart_data, total_cost = dc.display_cart(cart)
    if cart_data is None:
        return
    print(f"\n💵 Total Cost: ₹{total_cost}")

