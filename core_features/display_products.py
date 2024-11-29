# pc -> products_catalog, pe -> products_emoji
def display_products(pc: dict, pe: dict, category: str, ) -> None:
    print("\nCategory Options:")
    options = category.options # list of categories
    print(options)
    option = input("Choose category: ").strip().upper()
    print("\nAvailable products")
    for id, product in pc.products_catalog.items():# iterates over the products
        if option == '.' or id.startswith(option):
            print("---------------------------------------------")
            name = product["name"]
            description = product["description"]
            price = product["price"]
            stock = product["stock"]
            emoji = pe.products_emojis.get(name, "")

            print(f"- Product Name: {name} {emoji} | {id} \n- Description: {description} \n- Price: ₹{price} \n- Stock: {stock}")
    
    if option not in category.category_code:
        print("Invalid category selected. Please try again.")
    
