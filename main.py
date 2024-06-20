

class InventoryItem:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.item_id}: {self.name} - {self.quantity} units @ ${self.price:.2f} each"

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.item_id in self.items:
            print(f"Item with ID {item.item_id} already exists.")
        else:
            self.items[item.item_id] = item
            print(f"Item {item.name} added to inventory.")

    def remove_item(self, item_id):
        if item_id in self.items:
            removed_item = self.items.pop(item_id)
            print(f"Item {removed_item.name} removed from inventory.")
        else:
            print(f"Item with ID {item_id} not found.")

    def update_item(self, item_id, quantity=None, price=None):
        if item_id in self.items:
            item = self.items[item_id]
            if quantity is not None:
                item.quantity = quantity
            if price is not None:
                item.price = price
            print(f"Item {item.name} updated.")
        else:
            print(f"Item with ID {item_id} not found.")

    def view_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for item in self.items.values():
                print(item)



def add_new_item(inventory):
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    price = float(input("Enter item price: "))
    new_item = InventoryItem(item_id, name, quantity, price)
    inventory.add_item(new_item)

def remove_existing_item(inventory):
    item_id = input("Enter item ID to remove: ")
    inventory.remove_item(item_id)

def update_existing_item(inventory):
    item_id = input("Enter item ID to update: ")
    quantity = input("Enter new quantity (leave blank to skip): ")
    price = input("Enter new price (leave blank to skip): ")
    quantity = int(quantity) if quantity else None
    price = float(price) if price else None
    inventory.update_item(item_id, quantity, price)

def view_all_items(inventory):
    inventory.view_inventory()


def main():
    inventory = Inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add new item")
        print("2. Remove item")
        print("3. Update item")
        print("4. View all items")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_item(inventory)
        elif choice == '2':
            remove_existing_item(inventory)
        elif choice == '3':
            update_existing_item(inventory)
        elif choice == '4':
            view_all_items(inventory)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
