'''
Inventory Class for a Store
•	Create a class called Inventory with attributes:
        o	items: A dictionary to store items and their quantities.
•	Write methods to:
        o	Add items to the inventory with quantities.
        o	Remove items from the inventory.
        o	Display all items and their quantities.
•	Instantiate the Inventory class, add some items, remove an item, and list the remaining items.
'''

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"Added {quantity} {item}(s) to the inventory.")

    def remove_item(self, item, quantity):
        if item in self.items:
            if self.items[item] >= quantity:
                self.items[item] -= quantity
                print(f"Removed {quantity} {item}(s) from the inventory.")
                if self.items[item] == 0:
                    del self.items[item]  
            else:
                print(f"Error: Not enough {item}(s) in inventory to remove {quantity}.")
        else:
            print(f"Error: {item} not found in the inventory.")

    def display_items(self):
        if self.items:
            print("\nCurrent Inventory:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")
        else:
            print("The inventory is empty.")

inventory = Inventory()

inventory.add_item("Dew", 20)
inventory.add_item("Cadboury Dairy Milk", 80)
inventory.add_item("Nutella", 40)

inventory.display_items()

inventory.remove_item("Dew", 8)
inventory.remove_item("Nutella", 42)  

inventory.display_items()

inventory.remove_item("Cadboury Dairy Milk", 50)

inventory.display_items()