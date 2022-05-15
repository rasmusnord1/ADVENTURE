file = open('Text_support.txt')
line = file.readlines()

# SKRIV ALLA SAKER I EGNA FILER :) 
# glum inte adda gamestate till definitioner som kräver det :)

rooms = {
    'captains quarters': {'name': 'captains quarters', 'roomchoice': ['deck'], 'item': [], 'useitem' : [], 'use_item_on': [], 'desc' : line[7], 'lookat' : ['papers','radio','desk','bed']},
    'kitchen': {'name': 'kitchen', 'roomchoice': ['sleeping quarters', 'deck'], 'item': ['crowbar'], 'useitem' : [], 'use_item_on': [], 'desc' : line[9], 'lookat' : ['corner']},
    'sleeping quarters': {'name': 'sleeping quarters', 'roomchoice': ['kitchen','engine room'], 'item': 'key', 'useitem' : [], 'use_item_on': [], 'desc' : line[11], 'lookat' : ['bag']},
    'engine room': {'name': 'engine room', 'roomchoice': ['sleeping quarters'], 'item': [], 'useitem' : ['key','fuse'], 'use_item_on': ['locker', 'fusebox'], 'desc' : line[13], 'lookat' : ['engine','fusebox','locker']},
    'deck': {'name': 'deck', 'roomchoice': ['captains quarters', 'kitchen'], 'item': [], 'useitem' : ['toolbox','crowbar'], 'use_item_on': ['lifeboat','shipping container'], 'desc' : line[15], 'lookat' : ['lifeboat', 'shipping container']}
}
command_switch = {
    ('pickup','pick-up','take','get','grab','t'):'take',
    ('use','apply','operate','u'):'use',
    ('go','walk','run','leave','climb','g'):'go',
    ('look','inspect','investigate','view','l'):'look',
    ('help','h','hjälp',):'help',
    ('inventory', 'i'):'inventory'
}


gamestate = {}
commands = {}
gamestate['inventory'] = []
gamestate['current location'] = rooms['captains quarters']
gamestate['items taken'] = []
gamestate['shipping container'] = 'closed'
gamestate['locker'] = 'closed'
gamestate['electricity'] = 'off'
gamestate['lifeboat'] = 'broken'

# from parse_input import *

def parse_input(text_input):
    words = text_input.split(' ')
    helper_commands = ['at','to','in','through','by','the','and','but','toward','outside','inside','down','up','metal']
    for word in words[:]:
        if word in helper_commands: 
            words.remove(word)
    for command in command_switch:
        if words[0] in command:
            user_input = f'{command_switch[command]} {" ".join(words[1:])}' 
            #rest_input = " ".join(words[1:])
            return user_input#, rest_input # kanske användbart.

def inventory_check(preventTypeError):
    if gamestate['inventory'] == []:
        input('\nYou have nothing in your inventory.')
    else:
        inventory_text = (', ').join(gamestate['inventory'])
        input(f"\nThe following things are in your inventory: \n{inventory_text}")
    return main()


def end(ending_type):
    if ending_type == 'BAD':
        input(line_join(60))
    elif ending_type == 'NEUTRAL':
        input(line_join(62))
    elif ending_type == 'GOOD':
        input(line_join(64))
    return quit()

def usage_error():
    input('\nYou cannot do that here')
    return main()

def line_join(number):
    return f"\n{''.join(line[int(number)])}"

def can_pickup_item(item_to_pickup, gamestate):

    return True

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
    item_action_list = ['fuse','toolbox', 'key', 'crowbar']
    
     # Tror nog allt måste vara if-satser, då det inte går att appenda typ toolbox från input "key" i dictionary
    if item_used in item_action_list:
        if item_used == 'key':
            gamestate['current location']['item'].append('toolbox')
            gamestate['locker'] = 'open'
            input(line_join(50))
        elif item_used == 'crowbar':
            gamestate['current location']['item'].append('fuse')
            gamestate['shipping container'] = 'open'
            input(line_join(54))
        elif item_used == 'fuse':
            gamestate['electricity'] = 'on'
            input(line_join(56))
        elif item_used == 'toolbox':
            gamestate['lifeboat'] = 'fixed'
            input(line_join(52))
            
    else:
        input(item_text_list[item_used])
    return main()

def use_item(user_input):
    ending_check(user_input)
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
                # if can_use_item(user_input, gamestate):
                #     print('[TRIGGER] use item') #inte klar
                # if gamestate['current location'] == 'deck':
                #     gamestate['inventory'].remove('crowbar')
                #     print(line[...])

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
    input("\n"*3 + ''.join(line[68:81]))
    return main()


def look_check(user_input):
    lookat_input = user_input.split()[1:]
    lookat_input_text = " ".join(lookat_input)
    itemlocation_check = lookat_input_text in gamestate['current location']['lookat']

    lookat_list = {'desk': line_join(22), 'papers': line_join(22), 'bed': line_join(24), 'corner': line_join(27), 'engine': line_join(33), 'fusebox': line_join(35), 'lifeboat': line_join(42)}
    if itemlocation_check:
        if lookat_input_text in lookat_list:
            input(lookat_list[lookat_input_text])
            return main()
        elif lookat_input_text == 'corner' and 'crowbar' not in gamestate['items taken']:
            input(line_join(27))
            return main()
        elif lookat_input_text == 'bag' and 'key' not in gamestate['items taken']:
            input(line_join(30)) # NOT DONE
            return main()
        elif lookat_input_text == 'shipping container':
            if gamestate['shipping container'] == 'closed':
                input(line_join(44))
            if gamestate['shipping container'] == 'open':
                input(line_join(46))
        elif lookat_input_text == 'locker':
            if gamestate['locker'] == 'closed':
                input(line_join(37))
            if gamestate['locker'] == 'open':
                input(line_join(39))
        elif lookat_input_text == 'radio':
            if gamestate['electricity'] == 'off':
                input(line_join(20))
            if gamestate['electricity'] == 'on':
                end('GOOD')
        else:
            return usage_error()
    else:
        return usage_error()
    return main()



def ending_check(user_input):
    if 'use lifeboat' in user_input: 
        if gamestate['current location']['name'] == 'deck': 
            if gamestate['lifeboat'] == 'broken':
                return end('BAD')
            elif gamestate['lifeboat'] == 'fixed':
                return end('NEUTRAL')
    elif 'use radio' in user_input:
        if gamestate['electricity'] == 'off':
            input(line_join(20))
        elif gamestate['electricity'] == 'on':
            end('GOOD')






# from SupportingFiles import *


def main():
    cur_location = gamestate['current location']
    print('\n'*7 + f"{cur_location['name'].capitalize()}\n\n{''.join(cur_location['desc'])}")
    # print(line_join(52))

    gamestate['last_user_input'] = parse_input(input("Type 'h' for help.\n\nWhat would you like to do?\n>> ").lower())

    if gamestate['last_user_input'] == None:
        return usage_error()

    cmd_options = {'go': goto_location, 'take': pickup_item, 'use': use_item, 'look': look_check, 'help': help, 'inventory': inventory_check}

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


input("\n"*3 + f"{''.join(line[1:4])} \nPress enter to continue.")
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
