"""

Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems),
where the inventory parameter is a dictionary representing the player’s inventory
and the addedItems parameter is a list like dragonLoot.
The addToInventory() function should return a dictionary that represents the updated inventory.
Note that the addedItems list can contain multiples of the same item.

"""

def addToInventory(inventory, addedItems):
    items_to_be_added = {}
    for i in addedItems:
        if i not in items_to_be_added.keys():
            items_to_be_added[i] = 1
        else:
            items_to_be_added[i] = items_to_be_added.get(i) + 1

   # for i in
    items = list(inventory.keys())
    amount_of_item = list(inventory.values())
    total_number = 0

    print("Inventory:")

    for i in range(len(items)):
        print(amount_of_item[i], items[i])

    for number in amount_of_item:
        total_number += number

    print("Total number of items:", total_number)