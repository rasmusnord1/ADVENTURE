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
# gamestate['current location'] = 'captains quarters'



rooms = {
    'captains quarters': {'name': 'captains quarters', 'roomchoice': 'deck', 'item': 'crowbar', 'desc' : line[7]},
    'kitchen': {'name': 'kitchen', 'roomchoice': 'sleeping quarters', 'item': '[TEXT]', 'desc' : line[9]},
    'sleeping quarters': {'name': 'sleeping quarters', 'roomchoice': ['kitchen','engine room', 'deck'], 'item': '[TEXT]', 'desc' : line[11]},
    'engine room': {'name': 'engine room', 'roomchoice': 'sleeping quarters', 'item': '[TEXT]', 'desc' : line[13]},
    'deck': {'name': 'deck', 'roomchoice': ['captains quarters', 'sleeping quarters'], 'item': '[TEXT]', 'desc' : line[15]}
}
command_switch = {
    ('pickup','pick-up','take','get','grab'):'take',
    ('use','apply','operate'):'use',
    ('go','walk','run','leave','climb'):'go',
    ('look','inspect','view','l'):'look'
}



cur_location = rooms['captains quarters']

def dialogue():
    return

def parse_input(text_input):
    words = text_input.split(' ')
    helper_commands = ['at','to','in','through','by','the','and','but','inside','toward','outside','inside']
    for word in words[:]:
        if word in helper_commands: 
            words.remove(word)
    for command in command_switch:
        if words[0] in command:
            # if och sen för att använda ett item på en annan sak.
            text_output = f'{command_switch[command]} {" ".join(words[1:])}'
            ri_output = " ".join(words[1:])
            print(text_output)
            return text_output, ri_output


            # if '{}'.format(cur_location['item']) in text_input:
            #     ri_output = '{}'.format(cur_location['item'])
            #     print('{}'.format(commands[command]))
            #     return commands[command], ri_output
            # for roomcheck in rooms[cur_location['name']] or rooms[cur_location['roomchoice']]:
            #     if roomcheck in text_input:
            #         ri_output = roomcheck
            #         return commands[command], ri_output

            # return 
            # output = f'{commands[command]} {" ".join(words[1:])}'

            # print(output)
            # return output, None

def usage_error():
    print('You cannot do that here')

def can_pickup_item(text_output):
    print(f'{text_output}' == f"take {cur_location['item']}")
    return f'{text_output}' == f"take {cur_location['item']}"

def pickup_item(text_output):
    if can_pickup_item(text_output):
        print('bing')
        cur_item = cur_location['item']
        if cur_location['item'] == 'nothing':
            print(f"You've already picked up {cur_item}.")
            return
        gamestate['inventory'].append(cur_item)
        print(f"You picked up the {cur_item}.")
        cur_location['item'] = 'nothing'
    else:
        return usage_error()


def can_use_item(text_output, gamestate):
    if gamestate: #inte klar
        return 

def use_item(text_output, gamestate):
    if can_use_item(text_output, gamestate):
        print('[TRIGGER] use item') #inte klar
    if gamestate['current location'] == 'deck':
        gamestate['inventory'].remove('crowbar')
        print(line[...])

def can_goto_location(text_output):
    words = text_output.split()
    print(words[0])
    if words[0] == 'go':
        print(' '.join(words[1:]))
        print(cur_location['roomchoice'])
        print(' '.join(words[1:]) in cur_location['roomchoice'])
        return ' '.join(words[1:]) in cur_location['roomchoice']

def goto_location(text_output):
    if can_goto_location(text_output):
        words = text_output.split()
        print(words)
        cur_location = rooms[' '.join(words[1:])]
        print(f"You walk to the {cur_location['name']}") 
        return dialogue



# TESTING
print(cur_location['item'])
print(cur_location['roomchoice'])
# def goto_location(ri_output):
#     print(ri_output)
#     if ri_output in rooms[cur_location['roomchoice']]:
#         cur_location = rooms[ri_output]
#         print(cur_location)
#         return cur_location
#     else:
#         return usage_error









# def main(): #kanske ta bort funktionen
# #    main_menu()
#     print(f'\n\n{line[0]}')


#     # current location 
#     cur_location = 'captains quarters'
N = True
#def main_game():
while N == True:
#        print('You are in the {}.'.format(cur_location['name'], ))  # Print current location
#        print('This room contains {}.'.format(cur_location['item'], ))  # Print the item in the locations, BEHÖVS NOG INTE
        input(f"\n\n{''.join(line[1:4])} \nPress enter to continue.")
        
        print('\n'*7 + f"You are in the {(cur_location['name'])}.\n{''.join(cur_location['desc'])}")
        
        text_output, ri_output = parse_input(input('\n\nWhat would you like to do?\n>> '))
        
        if text_output == 'take item':
            pickup_item(text_output)
        elif text_output == 'use item':
            use_item(text_output)
        else:
            goto_location(text_output)
        
        N = False

commands['take item'] = {
    'perform': pickup_item(text_output)
}
# commands['use item'] = {
#     'perform': use_item()
# }

commands['goto location'] = {
    'perform': goto_location(text_output)
}



#print(main())
