from UsageError import *

file = open('Text_support.txt')
line = file.readlines()


def can_pickup_item(gamestate):

    user_input = gamestate['current user input']

    item_from_input = " ".join(user_input.split()[1:])
    
    if gamestate['current location']['item'] == '':
        return usage_error()

    elif item_from_input in gamestate['items taken']:

        input(f"You've already picked up {item_from_input}.")
        return

    could_pickup_item = item_from_input in gamestate['current location']['item']
    return could_pickup_item


def pickup_item(gamestate):

    user_input = gamestate['current user input']


    if can_pickup_item(gamestate):

        item_from_input = "".join(user_input.split()[1:])

        gamestate['inventory'].append(item_from_input)
        gamestate['items taken'].append(item_from_input)

        input(f"\nYou picked up the {item_from_input}.")
       
        return 

    else:
        return usage_error()