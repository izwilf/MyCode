import sys
from retailitem import RetailItem
def main():
    inventory = make_list()
    display_list(inventory)
def make_list():
    #Creates an empty list
    item_list = []
    description = "Jacket"
    units = 12
    price = "$59.95"
    number = 1
    items = RetailItem(description, units, price, number)
    item_list.append(items)
    description = "Designer Jeans"
    units = 40
    price = "$34.95"
    number = 2
    items = RetailItem(description, units, price, number)
    item_list.append(items)
    description = "Shirt"
    units = 20
    price = "$24.95"
    number = 3
    items = RetailItem(description, units, price, number)
    item_list.append(items)
    
    return item_list
def display_list(item_list):
    for description in item_list:
        print("Retail Item " + str(description.get_number()) + ":")
        print("Description: " + str(description.get_item_description()))
        print("Units in inventory: " + str(description.get_units()))
        print("Price: " + description.get_price())
        print()
main()