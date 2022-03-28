
class Inventory:
	armor = "Clothing"
	lockpick = False 



print('big')

yes = ["y", "yes"]
no = ["n", "no"]

ans = input(">>")

def main():
    main_menu()

    rooms = {
        'Captains quarters': {'name': 'Captains quarters', 'Down': 'Kitchen and dining', 'item': 'nothing'},
        'Kitchen and dining': {'name': 'Kitchen and dining', 'Up': 'Captains quarters', 'Down': 'Sleeping quarters',
                            'item': 'nothing'},
        'Sleeping quarters': {'name': 'Sleeping quarters', 'Up': 'Kitchen and dining', 'Down': 'Engine Room', 
                            'Outside': 'Deck', 'item': 'nothing'},
        'Engine Room': {'name': 'Engine Room', 'Up': 'Sleeping quarters', 'item': 'nothing'},
        'Deck': {'name': 'Deck', 'item': 'nothing'}
    }

    # current location 
    cur_location = rooms['Captains quarters']

    # current commands available to the player
    commands = ['North', 'South', 'West', 'East', 'Up', 'Down', 'Item']

    # Blank list for the inventory
    inventory = []




