from UsageError import *

file = open('Text_support.txt')
line = file.readlines()


rooms = {
    'captains quarters': {'name': 'captains quarters', 'roomchoice': ['deck'], 'item': [], 'useitem' : [], 'use_item_on': [], 'desc' : line[7], 'lookat' : ['papers','radio','desk','bed']},
    'kitchen': {'name': 'kitchen', 'roomchoice': ['sleeping quarters', 'deck'], 'item': ['crowbar'], 'useitem' : [], 'use_item_on': [], 'desc' : line[9], 'lookat' : ['corner']},
    'sleeping quarters': {'name': 'sleeping quarters', 'roomchoice': ['kitchen','engine room'], 'item': 'key', 'useitem' : [], 'use_item_on': [], 'desc' : line[11], 'lookat' : ['bag']},
    'engine room': {'name': 'engine room', 'roomchoice': ['sleeping quarters'], 'item': [], 'useitem' : ['key','fuse'], 'use_item_on': ['locker', 'fusebox'], 'desc' : line[13], 'lookat' : ['engine','fusebox','locker']},
    'deck': {'name': 'deck', 'roomchoice': ['captains quarters', 'kitchen'], 'item': [], 'useitem' : ['toolbox','crowbar'], 'use_item_on': ['lifeboat','shipping container'], 'desc' : line[15], 'lookat' : ['lifeboat', 'shipping container']}
}

def can_goto_location(gamestate):

    user_input = gamestate['current user input']

    words = user_input.split()

    is_input_in_roomchoice = (' ').join(words[1:]) in gamestate['current location']['roomchoice']

    return is_input_in_roomchoice

def goto_location(gamestate):

    user_input = gamestate['current user input']

    if can_goto_location(gamestate):

        words = user_input.split()
        gamestate['current location'] = rooms[' '.join(words[1:])]

        input(f"\nYou walk to the {gamestate['current location']['name']}") 

        return

    return usage_error()