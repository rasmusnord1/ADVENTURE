from gamestate import *
import time

file = open('Text_support.txt')
line = file.readlines()

#Text_support = "Text_support.txt"

#with open(Text_support) as f:
#    line = f.readlines()
# How to read: https://www.pythontutorial.net/python-basics/python-read-text-file/
# cmd+shift+7 for '#'



gamestate = {}
commands = {}
gamestate['inventory'] = []




rooms = {
    'captains quarters': {'name': 'captains quarters', 'roomchoice': 'deck', 'item': 'crowbar', 'useitem' : 'crowbar', 'use_item_on': 'fridge', 'desc' : line[7]},
    'kitchen': {'name': 'kitchen', 'roomchoice': 'sleeping quarters', 'item': '[TEXT]', 'useitem' : 'crowbar', 'use_item_on': 'fridge', 'desc' : line[9]},
    'sleeping quarters': {'name': 'sleeping quarters', 'roomchoice': ['kitchen','engine room', 'deck'], 'item': '[TEXT]', 'useitem' : 'crowbar', 'use_item_on': 'fridge', 'desc' : line[11]},
    'engine room': {'name': 'engine room', 'roomchoice': 'sleeping quarters', 'item': '[TEXT]', 'useitem' : 'crowbar', 'use_item_on': 'fridge', 'desc' : line[13]},
    'deck': {'name': 'deck', 'roomchoice': ['captains quarters', 'sleeping quarters'], 'item': '[TEXT]', 'useitem' : 'crowbar', 'use_item_on': 'fridge', 'desc' : line[15]}
}
command_switch = {
    ('pickup','pick-up','take','get','grab'):'take',
    ('use','apply','operate'):'use',
    ('go','walk','run','leave','climb'):'go',
    ('look','inspect','view'):'look',
    ('turn', 'put'):'turn'
}



gamestate['current location'] = rooms['captains quarters']



def parse_input(text_input):
    words = text_input.split(' ')
    helper_commands = ['at','to','in','through','by','the','and','but','toward','outside','inside','down','up']
    for word in words[:]:
        if word in helper_commands: 
            words.remove(word)
    for command in command_switch:
        if words[0] in command:
            # if och sen för att använda ett item på en annan sak.
            text_output = f'{command_switch[command]} {" ".join(words[1:])}' # använda command_switch?
            ri_output = " ".join(words[1:])
            # print(ri_output)
            # print(text_output)
            return text_output#, ri_output # kanske användbart.



def usage_error():
    input('\nYou cannot do that here')
    return main()

def can_pickup_item(text_output):
    print(f'{text_output}' == f"take {gamestate['current location']['item']}")
    return f'{text_output}' == f"take {gamestate['current location']['item']}"

def pickup_item(text_output):
    if can_pickup_item(text_output):
        print('bing')
        cur_item = gamestate['current location']['item']
        if gamestate['current location']['item'] == 'nothing':
            print(f"You've already picked up {cur_item}.")
            return main()
        gamestate['inventory'].append(cur_item)
        input(f"\nYou picked up the {cur_item}.")
        gamestate['current location']['item'] = 'nothing'
    else:
        return usage_error()


def use_item(text_output, gamestate):
    words = text_output.split()
    if words[1] in gamestate['inventory']:
        if 'use' and 'on' in words:
            if words[1] == gamestate['current location']['useitem']:
                if words[3] == gamestate['current location']['use_item_on']:
                    print(words, words[1], gamestate['inventory'])
                    input(f"\nYou succesfully used your {words[1]} on the {words[3]}.")
                    gamestate['inventory'].remove(words[1])
                    Success = gamestate['current location']['item_succes'] = True
                    return Success
                input("\nNothing happened.")
                return main()
            input("\nYou cannot use that item here.")
            return main()
        input("\nYou have to specify what to use the item on.")
        return main()
    input("\nYou don't have that item in your inventory.")
    return main()

# def use_item(text_output, gamestate):
#     if can_use_item(text_output, gamestate):
#         print('[TRIGGER] use item') #inte klar
#     if gamestate['current location'] == 'deck':
#         gamestate['inventory'].remove('crowbar')
#         print(line[...])

def can_goto_location(text_output):
    words = text_output.split()
    print(words[0])
    if words[0] == 'go':
        print(' '.join(words[1:]))
        print(gamestate['current location']['roomchoice'])
        print(' '.join(words[1:]) in gamestate['current location']['roomchoice'])
        return ' '.join(words[1:]) in gamestate['current location']['roomchoice']

def goto_location(text_output, gamestate):
    if can_goto_location(text_output):
        words = text_output.split()
        print(words)
        gamestate['current location'] = rooms[' '.join(words[1:])]
        input(f"\nYou walk to the {gamestate['current location']['name']}") 
        return main()
    return usage_error()

#Room-specific tasks
def radio(text_output):
    if 'on' and 'radio' in text_output:
        input(f"\n{''.join(line[20])}")
        return main()



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
        print('\n'*7 + f"You are in/on the {cur_location['name']}.\n{''.join(cur_location['desc'])}")
        
        print(cur_location['name'])
        print(cur_location['item'])
        print(cur_location['use_item_on'])
        print(cur_location['roomchoice'])

        text_output = parse_input(input('\n\nWhat would you like to do?\n>> ').lower())
        print('_____')
        print(text_output)
        if text_output == None:
            return usage_error()
        elif 'go' in text_output:
            return goto_location(text_output, gamestate)
        elif 'take' in text_output:
            return pickup_item(text_output)
        elif 'use' in text_output:
            return use_item(text_output, gamestate)
        elif 'turn' in text_output:
            return radio(text_output)
        else:
            usage_error()
        return






# def main(): #kanske ta bort funktionen
# #    main_menu()
#     print(f'\n\n{line[0]}')

input(f"\n\n{''.join(line[1:4])} \nPress enter to continue.")
main()

#     # current location 
#     cur_location = 'captains quarters'
Repeat = False
#def main_game():
# while Repeat == True:
# #        print('You are in the {}.'.format(cur_location['name'], ))  # Print current location
# #        print('This room contains {}.'.format(cur_location['item'], ))  # Print the item in the locations, BEHÖVS NOG INTE
        
#         print('\n'*7 + f"You are in/on the {(cur_location['name'])}.\n{''.join(cur_location['desc'])}")
        
#         text_output = parse_input(input('\n\nWhat would you like to do?\n>> ').lower())
#         print('_____')
#         print(text_output)
#         if text_output == None:
#             usage_error()
#         elif 'go' in text_output:
#             goto_location(text_output)
#         elif 'take' in text_output:
#             pickup_item(text_output)
#         elif 'use' in text_output:
#             use_item(text_output, gamestate)
#         elif 'turn' in text_output:
#             radio(text_output)
#         else:
#             usage_error()
        
#         print(cur_location['name'])
#         print(cur_location['item'])
#         print(cur_location['use_item_on'])
#         print(cur_location['roomchoice'])
        
        # Gamla commands av Linus:
        #
        # commands['take item'] = {
        #     'perform': pickup_item(text_output)
        # }
        # commands['use item'] = {
        #     'perform': use_item(text_output, gamestate)
        # }

        # commands['goto location'] = {
        #     'perform': goto_location(text_output)
        # }
        # 
        # Dessa går igenom en efter en. Vet inte hur de fungerar. 
        # If fungerar minst lika bra, men commands är kanske är snabbare. 
        #  - error från commands kommer före if (tror jag).


        #print(main())
