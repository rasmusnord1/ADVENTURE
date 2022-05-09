from gamestate import *
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
    'captains quarters': {'name': 'captains quarters', 'roomchoice': 'deck', 'item': '', 'useitem' : '', 'use_item_on': '', 'desc' : line[7], 'lookat' : ['papers','radio','desk']},
    'kitchen': {'name': 'kitchen', 'roomchoice': 'sleeping quarters', 'item': 'crowbar', 'useitem' : '', 'use_item_on': '', 'desc' : line[9]},
    'sleeping quarters': {'name': 'sleeping quarters', 'roomchoice': ['kitchen','engine room', 'deck'], 'item': 'key', 'useitem' : '', 'use_item_on': '', 'desc' : line[11]},
    'engine room': {'name': 'engine room', 'roomchoice': 'sleeping quarters', 'item': 'toolbox', 'useitem' : ['key','fuse'], 'use_item_on': ['locker', 'fuse box'], 'desc' : line[13]},
    'deck': {'name': 'deck', 'roomchoice': ['captains quarters', 'kitchen'], 'item': 'fuse', 'useitem' : ['toolbox','crowbar'], 'use_item_on': ['lifeboat','shipping container'], 'desc' : line[15]}
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
            print(user_input)
            return user_input#, rest_input # kanske användbart.



def usage_error():
    input('\nYou cannot do that here')
    return main()


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
    print('bing1')

    if can_pickup_item(user_input):
        item_from_input = "".join(user_input.split()[1:])
        print('bing')
        gamestate['inventory'].append(item_from_input)
        gamestate['items taken'].append(item_from_input)
        input(f"\nYou picked up the {item_from_input}.")
        return main()
    else:
        return usage_error()


def use_item(user_input):
    death(user_input)
    words = user_input.split()
    if words[1] in gamestate['inventory']:
        if 'use' and 'on' in words:
            if words[1] == gamestate['current location']['useitem']:
                if words[3] == gamestate['current location']['use_item_on']:
                    print(words, words[1], gamestate['inventory'])
                    input(f"\nYou succesfully used your {words[1]} on the {words[3]}.")
                    gamestate['inventory'].remove(words[1])
                    # Success = gamestate['current location']['item_succes'] = True
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
    print(words[0])
    if words[0] == 'go':
        print(' '.join(words[1:]))
        print(gamestate['current location']['roomchoice'])
        print(' '.join(words[1:]) in gamestate['current location']['roomchoice'])
        return ' '.join(words[1:]) in gamestate['current location']['roomchoice']

def goto_location(user_input):
    if can_goto_location(user_input):
        words = user_input.split()
        print(words)
        gamestate['current location'] = rooms[' '.join(words[1:])]
        input(f"\nYou walk to the {gamestate['current location']['name']}") 
        return main()
    return usage_error()

def help():
    input(''.join(line[57:70]))
    return main()


#Room-specific tasks
def look_check(user_input):
    lookat_input = user_input.split()[1:]
    itemlocation_check = "".join(lookat_input) in gamestate['current location']['lookat']
    print(lookat_input)
    print(itemlocation_check)
    if itemlocation_check:
        if 'radio' in user_input:
            input(f"\n{''.join(line[20])}")
            return main()
        elif itemlocation_check and 'desk' or 'papers' in user_input:
            # 
            input(''.join(line[22]))
            return main()
        
    return usage_error()

# if 'crowbar' in gamestate['items taken']:
#     input("You've already picked that shit up dawg cmon man do you have a bad memory? Are stewpid? INIT?"), main()

def death(user_input):
    words = user_input.split()
    print(words[0])
    print('use' and 'lifeboat' in words)
    print(gamestate['current location']['name'] == 'deck')
    if 'lifeboat' in words: 
        if gamestate['current location']['name'] == 'deck': 
            input('\nyou died lmao')
            return main()
        return usage_error()

# TESTING
print(gamestate['current location']['item'])
print(gamestate['current location']['roomchoice'])
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
    
    # print(cur_location['name'])
    # print(cur_location['item'])
    # print(cur_location['use_item_on'])
    # print(cur_location['roomchoice'])

    user_input = parse_input(input("Type 'help' for help.\n\nWhat would you like to do?\n>> ").lower())

    print(user_input)
    # print(rest_input)
    if user_input == None:
        return usage_error()
    print('bing1') 

    # cmd_options = {'go': goto_location(user_input), 'take': pickup_item(user_input), 'use': use_item(user_input), 'look': look_check(user_input), 'help': help()}

    # first_word_in_input = "".join(user_input.split()[0])
    # print('bing2')
    # print(first_word_in_input)
    # if first_word_in_input in cmd_options:
    #     cmd_options[first_word_in_input]
    death(user_input)
    # Eftersom commands inte funkade:
    if user_input == None:
        return usage_error()
    if 'go' in user_input:
        return goto_location(user_input)
    elif 'take' in user_input:
        return pickup_item(user_input)
    elif 'look' in user_input:
        return look_check(user_input)
    elif 'use' in user_input:
        return use_item(user_input)
    elif 'look' in user_input:
        return look_check(user_input)
    elif 'help' in user_input:
        return help()
    return usage_error()


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
