import numbers
#from gamestate import *
# import time

file = open('Text_support.txt')
line = file.readlines()

#Text_support = "Text_support.txt"

#with open(Text_support) as f:
#    line = f.readlines()
# How to read: https://www.pythontutorial.net/python-basics/python-read-text-file/
# cmd+shift+7 for '#'

# SKRIV ALLA SAKER I EGNA FILER :) 
# glum inte adda gamestate till definitioner som kräver det :)

rooms = {
    'captains quarters': {'name': 'captains quarters', 'roomchoice': ['deck'], 'item': '', 'useitem' : '', 'use_item_on': '', 'desc' : line[7], 'lookat' : ['papers','radio','desk','bed']},
    'kitchen': {'name': 'kitchen', 'roomchoice': ['sleeping quarters', 'deck'], 'item': 'crowbar', 'useitem' : '', 'use_item_on': '', 'desc' : line[9], 'lookat' : ['corner']},
    'sleeping quarters': {'name': 'sleeping quarters', 'roomchoice': ['kitchen','engine room', 'deck'], 'item': 'key', 'useitem' : '', 'use_item_on': '', 'desc' : line[11], 'lookat' : ['bag']},
    'engine room': {'name': 'engine room', 'roomchoice': ['sleeping quarters'], 'item': 'toolbox', 'useitem' : ['key','fuse'], 'use_item_on': ['locker', 'fuse box'], 'desc' : line[13]}, 'lookat' : ['engine','fuse box','locker'],
    'deck': {'name': 'deck', 'roomchoice': ['captains quarters', 'kitchen'], 'item': 'fuse', 'useitem' : ['toolbox','crowbar'], 'use_item_on': ['lifeboat','shipping container'], 'desc' : line[15], 'lookat' : ['lifeboat, shipping container']}
}
command_switch = {
    ('pickup','pick-up','take','get','grab','t'):'take',
    ('use','apply','operate','u'):'use',
    ('go','walk','run','leave','climb','g'):'go',
    ('look','inspect','investigate','view','l'):'look',
    ('help','h','hjälp',):'help'
    # (None):'N/A'
}


gamestate = {}
commands = {}
gamestate['inventory'] = []
gamestate['current location'] = rooms['captains quarters']
gamestate['items taken'] = []

# from parse_input import *

def parse_input(text_input):
    words = text_input.split(' ')
    helper_commands = ['at','to','in','through','by','the','and','but','toward','outside','inside','down','up']
    for word in words[:]:
        if word in helper_commands: 
            words.remove(word)
    for command in command_switch:
        if words[0] in command:
            user_input = f'{command_switch[command]} {" ".join(words[1:])}' 
            #rest_input = " ".join(words[1:])
            return user_input#, rest_input # kanske användbart.

def end(ending_type):
    if ending_type == 'GOOD':
        print('shit')
    elif ending_type == 'NEUTRAL':
        print('shit')
    elif ending_type == 'BAD':
        input(line_join(48))
    
    return quit()

def usage_error():
    input('\nYou cannot do that here')
    return main()

def line_join(number):
    return f"\n{''.join(line[int(number)])}"

# def can_pickup_item(item_to_pickup, gamestate):

#     return True

def can_pickup_item(user_input):
    item_from_input = "".join(user_input.split()[1:])
    if gamestate['current location']['item'] == '':
        return usage_error()
    elif item_from_input in gamestate['items taken']:
        input(f"You've already picked up {item_from_input}.")
        return main()
    could_pickup_item = item_from_input in gamestate['current location']['item']
    return could_pickup_item

def pickup_item(user_input):
    if can_pickup_item(user_input):
        item_from_input = "".join(user_input.split()[1:])
        gamestate['inventory'].append(item_from_input)
        gamestate['items taken'].append(item_from_input)
        input(f"\nYou picked up the {item_from_input}.")
        return main()
    else:
        return usage_error()


def use_item_success(item_used):
    item_text_list = {'crowbar': line_join(20), 'fuse': line_join(22), 'papers': line_join(22), 'bed': line_join(24)}
    item_action_list = ['fuse','toolbox', 'key']
    
    input(item_text_list[item_used]) # Tror nog allt måste vara if-satser, då det inte går att appenda typ toolbox från input "key" i dictionary
    if item_used in item_action_list:
        if item_used == 'fuse':
            return main()
        elif item_used == 'key':
            gamestate['inventory'].append('toolbox')
            gamestate['items taken'].append('toolbox')
            input(f"\nYou picked up the toolbox.")

    return main()

def use_item(user_input):
    death(user_input)
    words = user_input.split()
    if len(words) == 1:
        return usage_error()
    item_used_from_input = words[1]
    object_used_on_from_input = (' ').join(words[3:])
    
    # print("Following statements:\nwords[1] in gamestate['current location']['useitem']\nitem_index = gamestate['current location']['useitem'].index(words[1])\nwords[3] == gamestate['current location']['use_item_on'][item_index]\n")
    # print(words[1] in gamestate['current location']['useitem'])
    # item_index = gamestate['current location']['useitem'].index(words[1])
    # print(item_index)
    # print("gamestate: "+gamestate['current location']['use_item_on'][item_index])
    # print("from input: "+ (' ').join(words[3:]))
    # print((' ').join(words[3:]) == gamestate['current location']['use_item_on'][item_index])

    if words[1] in gamestate['inventory']:
        if 'use' and 'on' in words:
            if item_used_from_input in gamestate['current location']['useitem']:
                item_object_combination_check = gamestate['current location']['useitem'].index(item_used_from_input)
                if object_used_on_from_input == gamestate['current location']['use_item_on'][item_object_combination_check]:
                    input(f"\nYou succesfully used your {item_used_from_input} on the {object_used_on_from_input}.")
                    gamestate['inventory'].remove(item_used_from_input)
                    use_item_success(item_used_from_input)
                    return main()
                input("\nNothing happened.")
                return main()
            input("\nYou cannot use that item here.")
            return main()
        input("\nYou have to specify what to use the item on.")
        return main()
    input("\nYou don't have that item in your inventory.")
    return main()

# def use_item(user_input, gamestate):
#     if can_use_item(user_input, gamestate):
#         print('[TRIGGER] use item') #inte klar
#     if gamestate['current location'] == 'deck':
#         gamestate['inventory'].remove('crowbar')
#         print(line[...])

def can_goto_location(user_input):
    words = user_input.split()
    if words[0] == 'go':
        input_in_roomchoice_check = ' '.join(words[1:]) in gamestate['current location']['roomchoice']
        return input_in_roomchoice_check # Trash namn

def goto_location(user_input):
    if can_goto_location(user_input):
        words = user_input.split()
        gamestate['current location'] = rooms[' '.join(words[1:])]
        input(f"\nYou walk to the {gamestate['current location']['name']}") 
        return main()
    return usage_error()

def help(preventTypeError):
    input(''.join(line[57:70]))
    return main()


#Room-specific tasks
def look_check(user_input):
    lookat_input = user_input.split()[1:]
    lookat_input_text = "".join(lookat_input)
    itemlocation_check = lookat_input_text in gamestate['current location']['lookat']
    
    lookat_list = {'radio': line_join(20), 'desk': line_join(22), 'papers': line_join(22), 'bed': line_join(24)}

    if itemlocation_check:
        if lookat_input_text in lookat_list:
            input(lookat_list[lookat_input_text])
            return main()
        elif lookat_input_text == 'corner' and 'crowbar' not in gamestate['items taken']:
            input(line_join(27))
            return main()
        elif lookat_input_text == 'bag' and 'key' not in gamestate['items taken']:
            input(line_join) # NOT DONE
            return main()
    return usage_error()

# if 'crowbar' in gamestate['items taken']:
#     input("You've already picked that shit up dawg cmon man do you have a bad memory? Are stewpid? INIT?"), main()

def death(user_input):
    if 'use lifeboat' in user_input: 
        if gamestate['current location']['name'] == 'deck': 
            return end('BAD')
        return usage_error()

# TESTING

# def goto_location(ri_output):
#     print(ri_output)
#     if ri_output in rooms[cur_location['roomchoice']]:
#         cur_location = rooms[ri_output]
#         print(cur_location)
#         return cur_location
#     else:
#         return usage_error


def main():
    cur_location = gamestate['current location']
    print('\n'*7 + f"{cur_location['name'].capitalize()}\n\n{''.join(cur_location['desc'])}")
    # print(line_join(52))

    gamestate['last_user_input'] = parse_input(input("Type 'help' for help.\n\nWhat would you like to do?\n>> ").lower())

    if gamestate['last_user_input'] == None:
        return usage_error()

    cmd_options = {'go': goto_location, 'take': pickup_item, 'use': use_item, 'look': look_check, 'help': help}

    first_word_in_input = "".join(gamestate['last_user_input'].split()[0])

    if first_word_in_input in cmd_options:
        return cmd_options[first_word_in_input](gamestate['last_user_input'])

    return usage_error()
    # death(user_input)
    # # Eftersom commands inte funkade:
    # if user_input == None:
    #     return usage_error()
    # if 'go' in user_input:
    #     return goto_location(user_input)
    # elif 'take' in user_input:
    #     return pickup_item(user_input)
    # elif 'look' in user_input:
    #     return look_check(user_input)
    # elif 'use' in user_input:
    #     return use_item(user_input)
    # elif 'look' in user_input:
    #     return look_check(user_input)
    # elif 'help' in user_input:
    #     return help()
    # return usage_error()


        # alt: !!!!!!
        # cmd_options = {'go': goto_location(user_input), 'take': pickup_item(user_input), 'use': use_item(user_input), 'look': look_check(user_input), 'help': help()}        
        
        
        
        # print(cmd_options[user_input.split()[0]])
        # print(cmd_options['help'])
        # if user_input.split()[0] in cmd_options:
        #     return cmd_options[user_input.split()[0]]
        # else:
        #     return usage_error()
        # Från: https://stackoverflow.com/questions/17166074/most-efficient-way-of-making-an-if-elif-elif-else-statement-when-the-else-is-don 


input(f"\n\n{''.join(line[1:4])} \nPress enter to continue.")
main()


# def main(): #kanske ta bort funktionen
# #    main_menu()
#     print(f'\n\n{line[0]}')


#     # current location 
#     cur_location = 'captains quarters'
#def main_game():
# while Repeat == True:
# #        print('You are in the {}.'.format(cur_location['name'], ))  # Print current location
# #        print('This room contains {}.'.format(cur_location['item'], ))  # Print the item in the locations, BEHÖVS NOG INTE
        
#         print('\n'*7 + f"You are in/on the {(cur_location['name'])}.\n{''.join(cur_location['desc'])}")
        
#         user_input = parse_input(input('\n\nWhat would you like to do?\n>> ').lower())
#         print('_____')
#         print(user_input)
#         if user_input == None:
#             usage_error()
#         elif 'go' in user_input:
#             goto_location(user_input)
#         elif 'take' in user_input:
#             pickup_item(user_input)
#         elif 'use' in user_input:
#             use_item(user_input, gamestate)
#         elif 'turn' in user_input:
#             radio(user_input)
#         else:
#             usage_error()
        
#         print(cur_location['name'])
#         print(cur_location['item'])
#         print(cur_location['use_item_on'])
#         print(cur_location['roomchoice'])
        
        # Gamla commands av Linus:
        #
        # commands['take item'] = {
        #     'perform': pickup_item(user_input)
        # }
        # commands['use item'] = {
        #     'perform': use_item(user_input, gamestate)
        # }

        # commands['goto location'] = {
        #     'perform': goto_location(user_input)
        # }
        # 
        # Dessa går igenom en efter en. Vet inte hur de fungerar. 
        # If fungerar minst lika bra, men commands är kanske är snabbare. 
        #  - error från commands kommer före if (tror jag).


        #print(main())
