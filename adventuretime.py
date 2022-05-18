from ParseInput import *
from UsageError import *
from Help import *

from InventoryCheck import *
from PickupItem import *
from UseItem import *

from GotoLocation import *
from LookCheck import *


file = open('Text_support.txt')
line = file.readlines()


rooms = {
    'captains quarters': {'name': 'captains quarters', 'roomchoice': ['deck'], 'item': [], 'useitem' : [], 'use_item_on': [], 'desc' : line[7], 'lookat' : ['papers','radio','desk','bed']},
    'kitchen': {'name': 'kitchen', 'roomchoice': ['sleeping quarters', 'deck'], 'item': ['crowbar'], 'useitem' : [], 'use_item_on': [], 'desc' : line[9], 'lookat' : ['corner']},
    'sleeping quarters': {'name': 'sleeping quarters', 'roomchoice': ['kitchen','engine room'], 'item': 'key', 'useitem' : [], 'use_item_on': [], 'desc' : line[11], 'lookat' : ['bag']},
    'engine room': {'name': 'engine room', 'roomchoice': ['sleeping quarters'], 'item': [], 'useitem' : ['key','fuse'], 'use_item_on': ['locker', 'fusebox'], 'desc' : line[13], 'lookat' : ['engine','fusebox','locker']},
    'deck': {'name': 'deck', 'roomchoice': ['captains quarters', 'kitchen'], 'item': [], 'useitem' : ['toolbox','crowbar'], 'use_item_on': ['lifeboat','shipping container'], 'desc' : line[15], 'lookat' : ['lifeboat', 'shipping container']}
}


gamestate = {}

gamestate['current location'] = rooms['captains quarters']

gamestate['shipping container'] = 'closed'
gamestate['locker'] = 'closed'
gamestate['electricity'] = 'off'
gamestate['lifeboat'] = 'broken'

gamestate['inventory'] = []
gamestate['items taken'] = []

gamestate['current user input'] = ''


input("\n"*3 + f"{''.join(line[1:4])} \nPress enter to continue.")


def main():
    cur_location = gamestate['current location']
    print('\n'*7 + f"{cur_location['name'].capitalize()}\n\n{''.join(cur_location['desc'])}")

    gamestate['current user input'] = parse_input(input("Type 'h' for help.\n\nWhat would you like to do?\n>> ").lower())

    if gamestate['current user input'] == None:
        usage_error()
    else:
        cmd_options = {'go': goto_location, 'take': pickup_item, 'use': use_item, 'look': look_check, 'help': help, 'inventory': inventory_check}

        first_word_in_input = "".join(gamestate['current user input'].split()[0])


        if first_word_in_input in cmd_options:
            cmd_options[first_word_in_input](gamestate)

        else:
            usage_error()

while True:
    main()