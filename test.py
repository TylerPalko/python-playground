items = [
    "Apple", "Banana", "Carrot", "Desk", "Elephant", 
    "Fork", "Guitar", "Hat", "Ice cream", "Jacket", 
    "Kite", "Lemon", "Mango", "Notebook", "Octopus", 
    "Pencil", "Quilt", "Rainbow", "Sunflower", "Television"
]


def removeItem(rem_item):
    for i in items:
        if i == rem_item:
            items.remove(i)

rem = input('y or n ')

if rem == str('n'):
    print('hello')


#print(items)