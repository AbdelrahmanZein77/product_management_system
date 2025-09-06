import sys

# User data (basket, total price, deleted products)
user_basket = {}
user_price = 0
pro_delete = []

# Products (Juice)
product_juse = {
    "mango": {"price": 20, "quantity": 5},
    "banana": {"price": 15, "quantity": 7},
    "smothi": {"price": 20, "quantity": 10}
}

# Products (Eat)
product_eat = {
    "pasta": {"price": 20, "quantity": 5},
    "rice": {"price": 15, "quantity": 7},
    "meat": {"price": 20, "quantity": 10}
}

# Products (Sweet)
product_sweet = {
    "waffel": {"price": 20, "quantity": 5},
    "bancake": {"price": 15, "quantity": 7},
    "torta": {"price": 20, "quantity": 10}
}

# Show products in any category
def show_product(products):
    if not products:
        print("The products list is empty.")
    else:
        for name, data in products.items():
            price = data.get("price", "N/A")
            quantity = data.get("quantity", "N/A")
            print(f'{name} | price: {price} | quantity: {quantity}')

# Add a new product
def add_product(products):
    print("==========| ADD PRODUCT |===========")
    show_product(products)  # Show current products
    while True:
        name = input("Enter a product name (or 'no' to stop): ")
        if name in ["no", "n"]:  # Exit
            break
        if name in products:  # If product already exists
            print("This product already exists.")
            continue

        products[name] = {}  # Create new product as dictionary

        # Add price
        while True:
            try:
                price = float(input("Enter a price: "))
                if price <= 0:
                    print("Invalid price.")
                else:
                    products[name]["price"] = price
                    break
            except ValueError:
                print("Price must be a number.")

        # Add quantity
        while True:
            try:
                quantity = int(input("Enter a quantity: "))
                if quantity <= 0:
                    print("Invalid quantity.")
                else:
                    products[name]["quantity"] = quantity
                    print("Product added successfully.")
                    break
            except ValueError:
                print("Quantity must be an integer.")

# Edit product price
def edit_price(products):
    print("==========| EDIT PRICE |===========")
    show_product(products)
    while True:
        name = input("Enter a product name (or 'no' to stop): ")
        if name in ["no", "n"]:
            break
        if name not in products:
            print(f"Error: {name} not found.")
            continue

        print(f"Current price: {products[name]['price']}")
        while True:
            try:
                price = float(input("Enter new price: "))
                if price <= 0:
                    print("Invalid price.")
                else:
                    products[name]["price"] = price
                    print("Price updated.")
                    break
            except ValueError:
                print("Price must be a number.")

# Edit product quantity
def edit_quantity(products):
    print("==========| EDIT QUANTITY |===========")
    show_product(products)
    while True:
        name = input("Enter a product name (or 'no' to stop): ")
        if name in ["no", "n"]:
            break
        if name not in products:
            print(f"Error: {name} not found.")
            continue

        print(f"Current quantity: {products[name]['quantity']}")
        choice = input("1. Replace quantity / 2. Add to quantity: ")

        # Replace quantity
        while choice == "1":
            try:
                new_quantity = int(input("Enter new quantity: "))
                if new_quantity <= 0:
                    print("Invalid quantity.")
                else:
                    products[name]["quantity"] = new_quantity
                    print("Quantity updated.")
                    break
            except ValueError:
                print("Quantity must be an integer.")

        # Add to quantity
        while choice == "2":
            try:
                added_quantity = int(input("Enter quantity to add: "))
                if added_quantity <= 0:
                    print("Invalid quantity.")
                else:
                    products[name]["quantity"] += added_quantity
                    print("Quantity updated.")
                    break
            except ValueError:
                print("Quantity must be an integer.")

# Delete product
def delete_product(products):
    print("==========| DELETE PRODUCT |===========")
    show_product(products)
    while True:
        name = input("Enter a product name to delete (or 'no' to stop): ")
        if name in ["no", "n"]:
            break
        if name not in products:
            print(f"Error: {name} not found.")
        else:
            del products[name]  # Remove from dictionary
            pro_delete.append(name)  # Add to deleted list
            print(f"{name} deleted. Deleted list: {pro_delete}")

# Add products to user basket
def acount_user(products):
    global user_basket, user_price
    while True:
        show_product(products)  # Show available products
        name = input("Enter product name (or 'no' to stop): ")
        if name in ["e", "exit"]:  # Exit program
            sys.exit("Exiting...")
        if name in ["no", "n"]:  # Exit selection
            break
        if name not in products:  # If product not found
            print("Product not found.")
            continue

        # Enter quantity
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0 or quantity > products[name]["quantity"]:
                    print(f"Invalid quantity. Only {products[name]['quantity']} available.")
                else:
                    # Update basket and total price
                    user_price += products[name]["price"] * quantity
                    products[name]["quantity"] -= quantity
                    user_basket[name] = {"price": products[name]["price"], "quantity": quantity}
                    break
            except ValueError:
                print("Quantity must be a number.")
        break

# User interface for category selection
def user_interface():
    while True:
        print("1. Juice / 2. Sweet / 3. Eat")
        choice = input("Choose a category: ")
        if choice in ["e", "exit"]:
            sys.exit("Exiting...")
        if choice in ["no", "n"]:
            break
        elif choice == "1":
            acount_user(product_juse)
        elif choice == "2":
            acount_user(product_sweet)
        elif choice == "3":
            acount_user(product_eat)
        else:
            print("Invalid choice.")

    # Show user basket
    print("\n========= Basket =========")
    for name, data in user_basket.items():
        print(f"{name} | Price: {data['price']} | Quantity: {data['quantity']}")
    print(f"Total price: {user_price}")

# Choose category for any function (add, edit, delete, show)
def chose(func):
    print("1. Juice / 2. Sweet / 3. Eat")
    try:
        cat = int(input("Enter category number: "))
        if cat == 1:
            func(product_juse)
        elif cat == 2:
            func(product_sweet)
        elif cat == 3:
            func(product_eat)
        else:
            print("Invalid category.")
    except ValueError:
        print("You must enter a number.")

# Main menu (infinite loop until exit)
while True:
    print("=" * 50)
    print("""
1. Add product        2. Edit price
3. Edit quantity      4. Delete product
5. Show product       6. Make request
        7.show delete_product
    """)

    option = input("Choose an option (or 'no' to exit): ")

    if option in ["no", "n"]:
        break
    elif option == "1":
        chose(add_product)
    elif option == "2":
        chose(edit_price)
    elif option == "3":
        chose(edit_quantity)
    elif option == "4":
        chose(delete_product)
    elif option == "5":
        chose(show_product)
    elif option == "6":
        user_interface()
    elif option == "7":
        print(pro_delete)  # Show deleted products list
    else:
        print("Invalid option.")
