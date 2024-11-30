def display_menu():
    menu = {
        1: {"name": "Pizza", "price": 8.99},
        2: {"name": "Burger", "price": 5.49},
        3: {"name": "Pasta", "price": 7.99},
        4: {"name": "Salad", "price": 4.99},
        5: {"name": "Soda", "price": 1.99},
    }
    print("\n--- Menu ---")
    for item_id, item in menu.items():
        print(f"{item_id}. {item['name']} - ${item['price']:.2f}")
    return menu

def add_to_cart(menu, cart):
    item_id = int(input("Enter the item number to add to your cart: "))
    if item_id in menu:
        quantity = int(input(f"Enter quantity for {menu[item_id]['name']}: "))
        if item_id in cart:
            cart[item_id]['quantity'] += quantity
        else:
            cart[item_id] = {"name": menu[item_id]['name'], "price": menu[item_id]['price'], "quantity": quantity}
        print(f"Added {quantity} x {menu[item_id]['name']} to the cart.")
    else:
        print("Invalid item number. Please try again.")

def view_cart(cart):
    print("\n--- Your Cart ---")
    if not cart:
        print("Your cart is empty.")
    else:
        total = 0
        for item in cart.values():
            item_total = item['price'] * item['quantity']
            total += item_total
            print(f"{item['name']} - ${item['price']:.2f} x {item['quantity']} = ${item_total:.2f}")
        print(f"\nTotal: ${total:.2f}")

def place_order(cart):
    if not cart:
        print("Your cart is empty. Add items to place an order.")
    else:
        print("\nPlacing your order...")
        view_cart(cart)
        print("\nThank you for your order! It will be ready soon.")
        cart.clear()

def main():
    cart = {}
    while True:
        print("\n--- Online Food Ordering System ---")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Place Order")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            menu = display_menu()
        elif choice == "2":
            add_to_cart(menu, cart)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            place_order(cart)
        elif choice == "5":
            print("Thank you for using the Online Food Ordering System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()