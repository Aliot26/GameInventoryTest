import operator
# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
file_import_inventory = "import_inventory.csv"
file_export_inventory = "export_inventory.csv"

# Displays the inventory.


def display_inventory(inventory):
    print(" Inventory:")
    sumItems = 0
    for key in inventory.keys():
        print("%s   %s" % (inventory[key], key))
        sumItems += inventory[key]
    print("Total number of items: ", sumItems)


# Adds to the inventory dictionary a list of items from added_items.


def add_to_inventory(inventory, added_items):
    for lootItem in added_items:
        if lootItem in inventory:
            inventory[lootItem] += 1
        else:
            inventory.setdefault(lootItem, 1)
    return inventory

    # Takes your inventory and displays it in a well-organized table with
    # each column right-justified. The input argument is an order parameter (string)
    # which works as the following:
    # - None (by default) means the table is unordered
    # - "count,desc" means the table is ordered by count (of items in the inventory)
    #   in descending order
    # - "count,asc" means the table is ordered by count in ascending order


def print_table(inventory, order=None):
    if order == "count,desc":
        listSorted = [(k, inventory[k])
                      for k in sorted(inventory, key=inventory.get, reverse=True)]
        function_print(listSorted)
    elif order == "count,asc":
        listSorted = [(k, inventory[k])
                      for k in sorted(inventory, key=inventory.get, reverse=False)]
        function_print(listSorted)
    else:
        listNotSorted = inventory.items()
        function_print(listNotSorted)


def function_print(invList):
    hi = max(invList, key=len)
    maxLenStr = len(hi[0])
    a = 17
    print("Inventory: ")
    print("-"*(a+maxLenStr))
    print('{:>7}{:>{lenght}}'.format(
        "count", "item name", lenght=maxLenStr+9))
    print("-"*(a+maxLenStr))
    sumItems = 0
    for x in invList:
        print('{:>7}{:>{lenght}}'.format(
            x[1], x[0], lenght=maxLenStr+9))
        sumItems += x[1]
    print("-"*(a+maxLenStr))
    print("Total number of items: ", sumItems)

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).


def import_inventory(inventory, file_import_inventory):
    with open(file_import_inventory, "r") as f:
        newInv = f.read()
    newInv = newInv.split(',')
    newInv = add_to_inventory(inventory, newInv)
    print_table(newInv, order=None)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename):
    with open(filename, "w") as new_inv:
        for key, value in inventory.items():
            i = 0
            while i < value:
                new_inv.write(key + ",")
                i += 1
        size = new_inv.tell()
        new_inv.truncate(size - 1)


# Don't forget to delete this

"""display_inventory(inv)
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
print_table(inv)
import_inventory(inv)
export_inventory(inv)"""
