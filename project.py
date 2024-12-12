import random

items = [
    "Apple", "Banana", "Carrot", "Desk", "Elephant", 
    "Fork", "Guitar", "Hat", "Ice cream", "Jacket", 
    "Kite", "Lemon", "Mango", "Notebook", "Octopus", 
    "Pencil", "Quilt", "Rainbow", "Sunflower", "Television"
]


random_item = random.choice(items)

def removeItem():
        itemRem = input('What item would you like to remove? ')
        if itemRem == random_item:
             print('You Guessed the correct item when attempting to remove it!')
        while itemRem in items:
            if itemRem in items:
                    items.remove(itemRem)
        print(items)

def guess(prompt):
    guesses = 0
    while True:
        userInput = input(prompt)
        guesses += 1
        if userInput == 'R':
             removeItem()

        userInput = input('Please guess an item!: ')

        if userInput == random_item:
            print(f'It took you {guesses} guesses to get the correct answer! That\'s a {guesses}/20 chance!')
            break

        if userInput not in items:
            guesses -= 1

        if userInput != random_item:
            print('Sorry, that\'s wrong! \n Guesses:' + guesses)
            while userInput in items:
                if userInput in items:
                    items.remove(itemRem)
 


print(items)
guess('Please guess an item from the list above me, or type "R" to remove an item! \n')