import ParseInput
import InventoryCheck

from End import *

import UsageError

# from line_join import *

from PickupItem import *

from UseItem import *
from EndingCheck import *

from GotoLocation import *
import Help
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
command_switch_list = {
    ('pickup','pick-up','take','get','grab','t'):'take',
    ('use','apply','operate','u'):'use',
    ('go','walk','run','leave','climb','g'):'go',
    ('look','inspect','investigate','view','l'):'look',
    ('help','h','hjälp',):'help',
    ('inventory', 'i'):'inventory'
}


gamestate = {}

gamestate['current location'] = rooms['captains quarters']

gamestate['shipping container'] = 'closed'
gamestate['locker'] = 'closed'
gamestate['electricity'] = 'off'
gamestate['lifeboat'] = 'broken'

gamestate['inventory'] = []
gamestate['items taken'] = []





# def parse_input(text_input):

#     words = text_input.split(' ')
#     helper_commands = ['at','to','in','through','by','the','and','but','toward','outside','inside','down','up','metal']

#     for word in words[:]:

#         if word in helper_commands: 
#             words.remove(word)

#     for command_switch in command_switch_list:

#         if words[0] in command_switch:
#             parsed_text_input = f'{command_switch_list[command_switch]} {" ".join(words[1:])}' 

#             return parsed_text_input


# def inventory_check(gamestate):

#     if gamestate['inventory'] == []:
#         input('\nYou have nothing in your inventory.')

#     else:
#         inventory_text = (', ').join(gamestate['inventory'])
#         input(f"\nThe following things are in your inventory: \n{inventory_text}")
        
#     return main()


# def end(ending_type):
#     if ending_type == 'BAD':
#         input(line_join(60))

#     elif ending_type == 'NEUTRAL':
#         input(line_join(62))

#     elif ending_type == 'GOOD':
#         input(line_join(64))
        
#     return quit()


# def usage_error():

#     input('\nYou cannot do that here')
#     return main()


# def line_join(number):

#     return f"\n{''.join(line[int(number)])}"


# def can_pickup_item(gamestate):

#     user_input = gamestate['current user input']

#     item_from_input = " ".join(user_input.split()[1:])
    
#     if gamestate['current location']['item'] == '':
#         return usage_error()

#     elif item_from_input in gamestate['items taken']:

#         input(f"You've already picked up {item_from_input}.")
#         return main()

#     could_pickup_item = item_from_input in gamestate['current location']['item']
#     return could_pickup_item


# def pickup_item(gamestate):

#     user_input = gamestate['current user input']


#     if can_pickup_item(user_input):

#         item_from_input = "".join(user_input.split()[1:])

#         gamestate['inventory'].append(item_from_input)
#         gamestate['items taken'].append(item_from_input)

#         input(f"\nYou picked up the {item_from_input}.")
       
#         return main()

#     else:
#         return usage_error()


# def use_item_success(item_used, gamestate):

#     if item_used == 'key':

#         gamestate['current location']['item'].append('toolbox')
#         gamestate['locker'] = 'open'

#         input(line_join(50))

#     elif item_used == 'crowbar':

#         gamestate['current location']['item'].append('fuse')
#         gamestate['shipping container'] = 'open'

#         input(line_join(54))

#     elif item_used == 'fuse':

#         gamestate['electricity'] = 'on'

#         input(line_join(56))
        
#     elif item_used == 'toolbox':

#         input(line_join(52))

#         end('NEUTRAL')

#     return main()

# def use_item(gamestate):

#     user_input = gamestate['current user input']


#     ending_check(user_input)
#     words = user_input.split()

#     if len(words) == 1:
#         return usage_error()
        
#     item_used_from_input = words[1]
#     object_used_on_from_input = (' ').join(words[3:])
    
#     if words[1] in gamestate['inventory']:
#         if 'use' and 'on' in words:

#             if item_used_from_input in gamestate['current location']['useitem']:

#                 item_object_combination_check = gamestate['current location']['useitem'].index(item_used_from_input)

#                 if object_used_on_from_input == gamestate['current location']['use_item_on'][item_object_combination_check]:

#                     input(f"\nYou succesfully used your {item_used_from_input} on the {object_used_on_from_input}.")
#                     gamestate['inventory'].remove(item_used_from_input)

#                     use_item_success(item_used_from_input, gamestate)

#                     return main()

#                 input("\nNothing happened.")
#                 return main()

#             input("\nYou cannot use that item here.")
#             return main()

#         input("\nYou have to specify what to use the item on.")
#         return main()

#     input("\nYou don't have that item in your inventory.")
#     return main()


# def can_goto_location(gamestate):

#     user_input = gamestate['current user input']

#     words = user_input.split()

#     if words[0] == 'go':
#         is_input_in_roomchoice = (' ').join(words[1:]) in gamestate['current location']['roomchoice']

#         return is_input_in_roomchoice

# def goto_location(gamestate):

#     user_input = gamestate['current user input']

#     if can_goto_location(gamestate):

#         words = user_input.split()
#         gamestate['current location'] = rooms[' '.join(words[1:])]

#         input(f"\nYou walk to the {gamestate['current location']['name']}") 

#         return main()

#     return usage_error()


# def help(preventTypeError):

#     input("\n"*3 + ''.join(line[68:81]))

#     return main()


# def look_check(gamestate):

#     user_input = gamestate['current user input']

#     lookat_input = user_input.split()[1:]
#     lookat_input_text = " ".join(lookat_input)

#     itemlocation_check = lookat_input_text in gamestate['current location']['lookat']

#     lookat_object_list = {'desk': line_join(22), 'papers': line_join(22), 'bed': line_join(24), 'corner': line_join(27), 'engine': line_join(33), 'fusebox': line_join(35), 'lifeboat': line_join(42)}
    
#     if itemlocation_check:

#         if lookat_input_text in lookat_object_list:

#             input(lookat_object_list[lookat_input_text])
#             return main()

#         elif lookat_input_text == 'corner' and 'crowbar' not in gamestate['items taken']:

#             input(line_join(27))
#             return main()

#         elif lookat_input_text == 'bag' and 'key' not in gamestate['items taken']:

#             input(line_join(30)) 
#             return main()

#         elif lookat_input_text == 'shipping container':

#             if gamestate['shipping container'] == 'closed':
#                 input(line_join(44))

#             elif gamestate['shipping container'] == 'open':
#                 input(line_join(46))


#         elif lookat_input_text == 'locker':

#             if gamestate['locker'] == 'closed':
#                 input(line_join(37))

#             elif gamestate['locker'] == 'open' and 'toolbox' not in gamestate['items taken']:
#                 input(line_join(39))

#             else:
#                 return usage_error()

#         elif lookat_input_text == 'radio':

#             if gamestate['electricity'] == 'off':
#                 input(line_join(20))

#             elif gamestate['electricity'] == 'on':
#                 end('GOOD')
        
#         else:
#             return usage_error()
#     else:
#         return usage_error()
#     return main()


# def ending_check(gamestate):

#     user_input = gamestate['current user input']

#     if 'use lifeboat' in user_input: 

#         if gamestate['current location']['name'] == 'deck': 
#             return end('BAD')

#     elif 'use radio' in user_input and gamestate['current location']['name'] == 'captains quarters':

#         if gamestate['electricity'] == 'off':
#             input(line_join(20))
#             return main()

#         elif gamestate['electricity'] == 'on':
#             return end('GOOD')






def main():
    cur_location = gamestate['current location']
    print('\n'*7 + f"{cur_location['name'].capitalize()}\n\n{''.join(cur_location['desc'])}")

    print(ParseInput.parse_input('shit'))

    gamestate['current user input'] = ParseInput.parse_input(input("Type 'h' for help.\n\nWhat would you like to do?\n>> ").lower())

    if gamestate['current user input'] == None:
        return UsageError(main)

    cmd_options = {'go': goto_location, 'take': pickup_item, 'use': use_item, 'look': look_check, 'help': Help.help, 'inventory': InventoryCheck}

    first_word_in_input = "".join(gamestate['current user input'].split()[0])
    # Tar och delar upp 'current user input' till en lista och tar ut första ordet. Sedan gör join. delen att det första ordet görs om till en string igen.

    print(cmd_options[first_word_in_input](gamestate))

    if first_word_in_input in cmd_options:
        return cmd_options[first_word_in_input](gamestate, main)

    return UsageError()





input("\n"*3 + f"{''.join(line[1:4])} \nPress enter to continue.")

main()