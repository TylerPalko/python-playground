# By Tyler Palko

import random

items_large = [ # this was a larger list of items I used off video, this was too big for a 1 min video.
    "apple", "banana", "carrot", "desk", "elephant", 
    "fork", "guitar", "hat", "ice cream", "jacket", 
    "kite", "lemon", "mango", "notebook", "octopus", 
    "pencil", "quilt", "rainbow", "sunflower", "television"
]

items = [
    "apple", "banana", "carrot", "desk", "elephant", 
    "fork"]

# Defines what to do if a user decides to remove an item.
def removeItem(item):
    if item not in items:
        print('This item was either already removed, misstyped, or it was never in the list!')
    for i in items:
        if item in i == item:
            items.remove(i)

random_item = random.choice(items) # Select our random item that is supposed to be guessed by the user.
guesses = 0


print(items)
remChoice = input('Remove items before we start to make the game faster/ easier? (y/n): ') # Prompt the user if they want to remove an item

#if the user chooses to remove an item this script runs
while remChoice == "y":
    removeItem(input('What item would you like to remove? '))
    if input('Remove more items? (y/n): ') == "n": # ask the user if they want to remove more then one item, if they dont we move onto the game.
        break

while True:
    print(items)
    print('You have guessed ' + str(guesses) + ' times!')
    userInput = input('Please guess an item, or type exit to give up and get the answer!: ')

    # If the user types "exit" that means they give up and we output the answer and the ammount of guesses that they did
    if userInput == str("exit"):
        print('The answer was ' + random_item + ', and you gave up after ' + str(guesses) + ' guesses.')
        break
    
    #if the user gets the corect word we tell them so and tell them how many guesses they had
    if userInput == str(random_item):
        guesses += 1
        print('You got it correct after ' + str(guesses) + ' guesses!')
        break
    
    # if the user inputed an item that was not in the list then we output this
    if userInput not in items:
        print('This item is not in the list or you mistyped it.')
    # If the user guessed incorectly then we output this
    elif userInput != random_item:
        guesses += 1
        print('Sorry, thats wrong!')