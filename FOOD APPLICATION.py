import random

# Admin data (food items) stored in a list of dictionaries
food_items = []

# User data (registered users) stored in a list of dictionaries
users = []

# List to store user orders
user_orders = []

# Admin password (change to a secure password)
admin_password = "admin123"

# Function to generate a random FoodID
def generate_food_id():
    return random.randint(1000, 9999)

# Function for admin login
def admin_login():
    password = input("Enter Admin Password: ")
    if password == admin_password:
        print("Admin login successful.")
        admin_interface()
    else:
        print("Admin login failed. Please try again.")

# Admin Interface
def admin_interface():
    while True:
        print("\nAdmin Interface")
        print("1. Add Food Item")
        print("2. Edit Food Item")
        print("3. View Food Menu")
        print("4. Remove Food Item")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_food_item()
        elif choice == "2":
            edit_food_item()
        elif choice == "3":
            view_food_menu()
        elif choice == "4":
            remove_food_item()
        elif choice == "5":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

# Function for adding a food item (for the admin)
def add_food_item():
    food_item = {}
    food_item["FoodID"] = generate_food_id()
    food_item["name"] = input("Enter Food Name: ")
    food_item["quantity"] = input("Enter Quantity: ")
    food_item["price"] = float(input("Enter Price (INR): "))
    food_item["discount"] = float(input("Enter Discount (%): "))
    food_item["stock"] = int(input("Enter Stock Quantity: "))
    food_items.append(food_item)
    print("Food item added successfully!")

# Function for editing a food item (for the admin)
def edit_food_item():
    food_id = int(input("Enter FoodID to edit: "))
    for food_item in food_items:
        if food_item["FoodID"] == food_id:
            print(f"Editing Food Item {food_item['name']}:")
            food_item["name"] = input("Enter new Food Name: ")
            food_item["quantity"] = input("Enter new Quantity: ")
            food_item["price"] = float(input("Enter new Price (INR): "))
            food_item["discount"] = float(input("Enter new Discount (%): "))
            food_item["stock"] = int(input("Enter new Stock Quantity: "))
            print(f"Food item with FoodID {food_id} edited successfully.")
            return
    print(f"Food item with FoodID {food_id} not found.")

# Function for removing a food item (for the admin)
def remove_food_item():
    food_id = int(input("Enter FoodID to remove: "))
    for food_item in food_items:
        if food_item["FoodID"] == food_id:
            food_items.remove(food_item)
            print(f"Food item with FoodID {food_id} removed successfully.")
            return
    print(f"Food item with FoodID {food_id} not found.")

# Function for user registration
def user_register():
    print("\nUser Registration")
    user = {}
    user["full_name"] = input("Full Name: ")
    user["phone_number"] = input("Phone Number: ")
    user["email"] = input("Email: ")
    user["address"] = input("Address: ")
    user["password"] = input("Password: ")
    users.append(user)
    print("Registration successful!")

# Function for user login
def user_login():
    email = input("Enter your Email: ")
    password = input("Enter your Password: ")
    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"Welcome, {user['full_name']}!")
            user_interface(user)
            return
    print("Login failed. Please check your credentials.")

# User Interface
def user_interface(user):
    while True:
        print("\nUser Interface")
        print("1. Place New Order")
        print("2. Order History")
        print("3. Update Profile")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            place_new_order()
        elif choice == "2":
            view_order_history(user)
        elif choice == "3":
            update_profile(user)
        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

# Function for placing a new order (for the user)
def place_new_order():
    print("\nPlace New Order")
    print("Available Food Items:")
    for index, item in enumerate(menu_items, start=1):
        print(f"{index}. {item['name']} ({item['quantity']}) [INR {item['price']}]")

    user_order = input("Enter the numbers of the items you want to order (e.g., 1 2 3): ").split()
    total_price = 0
    order_summary = []

    for item_number in user_order:
        item_number = int(item_number)
        if 1 <= item_number <= len(menu_items):
            menu_item = menu_items[item_number - 1]
            order_summary.append(f"{menu_item['name']} ({menu_item['quantity']}) [INR {menu_item['price']}]")
            total_price += menu_item['price']
        else:
            print(f"Invalid item number: {item_number}")

    if order_summary:
        user_orders.append({'items': order_summary, 'total_price': total_price})
        print("Order placed successfully!")
    else:
        print("No items selected for the order.")

# Function for viewing order history (for the user)
def view_order_history(user):
    print("\nOrder History for", user["full_name"])
    for i, order in enumerate(user_orders, start=1):
        print(f"Order {i}:")
        for item in order["items"]:
            print(item)
    print(f"Total Price: INR {order['total_price']}\n")

# Function for updating user profile (for the user)
def update_profile(user):
    print("\nUpdate Profile for", user["full_name"])
    user["full_name"] = input("Full Name: ")
    user["phone_number"] = input("Phone Number: ")
    user["email"] = input("Email: ")
    user["address"] = input("Address: ")
    user["password"] = input("New Password: ")
    print("Profile updated successfully.")

# Define the menu items
menu_items = [
    {"name": "Tandoori Chicken", "quantity": "4 pieces", "price": 240},
    {"name": "Vegan Burger", "quantity": "1 Piece", "price": 320},
    {"name": "Truffle Cake", "quantity": "500gm", "price": 900}
]

# Function for the main program loop
def main():
    while True:
        print("\nWelcome to the Food Ordering App")
        print("1. Admin Login")
        print("2. User Registration")
        print("3. User Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_login()
        elif choice == "2":
            user_register()
        elif choice == "3":
            user_login()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

   
