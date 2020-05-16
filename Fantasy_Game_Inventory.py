"""
You are creating a fantasy video game.
The data structure to model the player’s inventory will be a dictionary
where the keys are string values describing the item in the inventory
and the value is an integer value detailing how many of that item the player has.
For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

"""

def displayInventory(inventory):
    items = list(inventory.keys())
    amount_of_item = list(inventory.values())
    total_number = 0

    print("Inventory:")

    for i in range(len(items)):
        print(amount_of_item[i], items[i])

    for number in amount_of_item:
        total_number += number

    print("Total number of items:", total_number)


displayInventory({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} )

# solution way

def displayInventorys(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
    print("Total number of items: " + str(item_total))


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
    for i in items_to_be_added.keys():
        if
    displayInventory(inventory)

