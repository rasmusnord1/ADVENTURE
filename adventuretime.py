yes = ["y", "yes"]
no = ["n", "no"]

#ans = input("\n>> ")

Text_support = "Text_support.txt"

with open(Text_support) as f:
    line = f.readlines()
# How to read: https://www.pythontutorial.net/python-basics/python-read-text-file/


def main(): #kanske ta bort funktionen
#    main_menu()
    print(line[0])
    rooms = {
        'captains quarters': {'name': 'captains quarters', 'down': 'deck', 'items': '[TEXT]', 'desc' : 'line[1]'},
        'kitchen': {'name': 'kitchen', 'down': 'sleeping quarters', 'items': '[TEXT]', 'desc' : 'line[2]'},
        'sleeping quarters': {'name': 'sleeping quarters', 'up': 'kitchen', 'down': 'engine room','outside': 'deck', 'items': '[TEXT]', 'desc' : 'line[3]'},
        'engine room': {'name': 'engine room', 'up': 'sleeping quarters', 'items': '[TEXT]', 'desc' : 'line[4]'},
        'deck': {'name': 'deck', 'inside1': 'captains quarters', 'inside2': 'sleeping quarters', 'items': '[TEXT]', 'desc' : 'line[5]'}
    }

    # current location 
    cur_location = rooms['captains quarters']

    commands = ['up', 'down', 'outside', 'inside' 'inventory', 'key', 'toolbox', 'crowbar', 'fuse', 'food']

    inventory = []

#def main_game():
    while True:
        print('You are in the {}.'.format(cur_location['name'], ))  # Print current location
        print('This room contains {}.'.format(cur_location['item'], ))  # Print the item in the locations, BEHÖVS NOG INTE


        command = input('\nWhat would you like to do?').strip()  # Get player command input
        if command in commands:

            if command in cur_location:
                cur_location = rooms[cur_location[command]]

            if command in 'bing':
                inventory.append(rooms[cur_location[command]])

        elif command.lower() == 'quit':  
            print('You quit the game.')
            break
        else:
            # if invalid command is given
            print('The loneliness of this place must be getting to you. Please try something else.')
    print()

print(main_game())