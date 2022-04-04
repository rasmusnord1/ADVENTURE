yes = ["y", "yes"]
no = ["n", "no"]

ans = input("\n>> ")


def main(): #kanske ta bort funktionen
#    main_menu()

    rooms = {
        'captains quarters': {'name': 'captains quarters', 'down': 'kitchen', 'outside': 'deck', 'items': '[insert text]', 'desc' : '[insert text]'},
        'kitchen': {'name': 'kitchen', 'up': 'captains quarters', 'down': 'sleeping quarters', 'items': '[insert text]', 'desc' : '[insert text]'},
        'sleeping quarters': {'name': 'sleeping quarters', 'up': 'kitchen', 'down': 'engine room','outside': 'deck', 'items': '[insert text]', 'desc' : '[insert text]'},
        'engine room': {'name': 'engine room', 'up': 'sleeping quarters', 'items': '[insert text]', 'desc' : '[insert text]'},
        'deck': {'name': 'deck', 'items': '[insert text]', 'desc' : '[insert text]'}
    }

    # current location 
    cur_location = rooms['captains quarters']

    # commands available to the player
    commands = ['up', 'down', 'outside', 'inventory', 'key', 'toolbox', 'crowbar', 'fuse', 'food']

    # Blank list for the inventory
    inventory = []

#def main_game():
    while True:
        print('You are in the {}.'.format(current_loc['name'], ))  # Print current location
        print('This room contains {}.'.format(current_loc['item'], ))  # Print the item in the locations


        command = input('\nWhat would you like to do?').strip()  # Get player command input
        if command in commands:

            if command in current_loc:
                current_loc = rooms[current_loc[command]]

            if command in 'bing':
                inventory.append(rooms[current_loc[command]])

        elif command.lower() == 'quit':  
            print('You quit the game.')
            break
        else:
            # if invalid command is given
            print('The loneliness of this place must be getting to you. Please try something else.')
    print()

print(main_game())