# Dictionary to store the inventory
inventory = {}

# Displays all items in the inventory
def view_inventory():
    print("\n--- Current Inventory: ---")
# checks if inventory is empty if not loops through every item and value in the inventory
    if len(inventory) == 0:
        print("Inventory is empty.\n")
        return

    for item in inventory:
        print(item, ":", inventory[item])
    print()
# allows user to add items to the inventory
def add_item():
    item = input("Enter item name: ").lower()
# checks if the item being added to the inventory is already in stock and prompts user to use the proper function if so, if not add the item to the inventory
    if item in inventory:
        print("Item already exists! use update option instead.\n")
        return

    qty = int(input("Enter quantity: "))
    inventory[item] = qty
    print("Item added!\n")
# allows the user to modify the quantity of items in the inventory
def update_item():
    item = input("Enter item to update: ").lower()
# checks if the item is in the inventory if it is then the user can add the item if not it lets the user know
    if item not in inventory:
        print("Item not found.\n")
        return

    qty = int(input("Enter new quantity: "))
    inventory[item] = qty
    print("Item updated!\n")
# allows user to remove items from the inventory
def remove_item():
    item = input("Enter item to remove: ").lower()
# checks if the item is in the inventory, if it is then it proceeds with removing it, if not then it lets the user know
    if item in inventory:
        del inventory[item]
        print("Item removed!\n")
    else:
        print("Item not found.\n")
# identifies and displays items below a threshold specified by the user
def check_low_stock():
    limit = int(input("Enter Threshold for low stock: "))
# loops through every key and value in the inventory to check if any item amounts are below the user threshold
# if there is then it prints out all items and the amount of each in low stock, if not then it lets the user know there is no low stock items
    print("\n--- Current low stock items: ---")
    found = False

    for item in inventory:
        if inventory[item] < limit:
            print(item, ":", inventory[item])
            found = True

    if not found:
        print("No low stock items.")
    print()
# creates the menu interface
def menu():
# the user interface continuously prints out after every choice the user makes until choosing the exit option
# allows the user to call functions by typing the number associated with it in the menu
    while True:
        print("------ MENU ------")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Check Low Stock")
        print("6. Exit")
        print("------------------\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            add_item()

        elif choice == "3":
            update_item()

        elif choice == "4":
            remove_item()

        elif choice == "5":
            check_low_stock()

        elif choice == "6":
            print("Goodbye!")

            break
        else:
            print("Invalid choice. Try again.\n")

# starts the programs menu
menu()

