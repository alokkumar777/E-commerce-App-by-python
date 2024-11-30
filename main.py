from products import products_catalog as pc
from products import products_emoji as pe
from core_features.category import category
from core_features import add_to_cart as atc
from core_features import display_products as dp
from core_features import place_order as po
from core_features import remove_from_cart as rfc
from core_features import view_cart as vc
from core_features import view_order_history as voh

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
    7. Search Product
    8. Save and Exit
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
                    vc.view_cart(cart)
                case 4:
                    rfc.remove_from_cart(pc, cart)
                case 5:
                    place_order()
                case 6:
                    view_order_history()
                case 7:
                    search_product()
                case 8:
                    save_data()
                    print("Exiting the system. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please select an option from 1 to 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

main_menu()

