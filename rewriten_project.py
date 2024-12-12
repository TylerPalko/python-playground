# By Tyler Palko

import random

items = [
    "apple", "banana", "carrot", "desk", "elephant", 
    "fork", "guitar", "hat", "ice cream", "jacket", 
    "kite", "lemon", "mango", "notebook", "octopus", 
    "pencil", "quilt", "rainbow", "sunflower", "television"
]

# Defines what to do if a user decides to remove an item.
def removeItem(item):
    if item not in items:
        print('This item was either already removed, misstyped, or it was never in the list!')
    for i in items:
        if item in i == item:
            items.remove(i)

random_item = random.choice(items)
guesses = 0


print(items)
remChoice = input('Remove items before we start to make the game faster/ easier? (y/n): ')


while remChoice == "y":
    removeItem(input('What item would you like to remove? '))
    if input('Remove more items? (y/n): ') == "n":
        break

while True:
    print(items)
    print(guesses)
    userInput = input('Please guess an item, or type exit to give up and get the answer!: ')
        
    if userInput == str("exit"):
        print('The answer was ' + random_item + ', and you gave up after ' + str(guesses) + ' guesses.')
        break

    if userInput == str(random_item):
        guesses += 1
        print('You got it correct after ' + str(guesses) + ' guesses!')
        break
    
    if userInput not in items:
        print('This item is not in the list or you mistyped it.')

    elif userInput != random_item:
        guesses += 1
        print('Sorry, thats wrong!')