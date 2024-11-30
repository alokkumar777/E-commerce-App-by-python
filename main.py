from products import products_catalog as pc
from products import products_emoji as pe
from core_features.category import category
from core_features import add_to_cart as atc
from core_features import display_products as dp
from core_features import place_order as po
from core_features import remove_from_cart as rfc
from core_features import view_cart as vc
from core_features import view_order_history as voh
from core_features import display_cart as dc
from core_features import cancel_order as co

cart = []
order_history = []

def main_menu():
    while True:
        menu = """
    E-Commerce System
    1. View Products
    2. Add to Cart
    3. View Cart
    4. Remove from Cart
    5. Place Order
    6. View Order History
    7. Cancel Order
    8. Exit
    """
        print(menu)


        try:
            choice = int(input("Enter your choice (1-9): "))
            match choice:
                case 1:
                    dp.display_products(pc, pe, category)
                case 2:
                    atc.add_to_cart(pc, cart)
                case 3:
                    vc.view_cart(dc, cart)
                case 4:
                    rfc.remove_from_cart(pc, cart)
                case 5:
                    po.place_order(dc, cart, order_history)
                case 6:
                    voh.view_order_history(order_history)
                case 7:
                    co.cancel_order(order_history)
                case 8:
                    print("Exiting the system. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please select an option from 1 to 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

main_menu()

