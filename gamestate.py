file = open('Text_support.txt')
line = file.readlines()

gamestate = {}
gamestate['inventory'] = []
gamestate['current location'] = 'captains quarters'

rooms = {
    'captains quarters': {'name': 'captains quarters', 'roomchoice': 'deck', 'item': 'crowbar', 'desc' : 'line[10]'},
    'kitchen': {'name': 'kitchen', 'roomchoice': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[2]'},
    'sleeping quarters': {'name': 'sleeping quarters', 'roomchoice': ['kitchen','engine room', 'deck'], 'item': '[TEXT]', 'desc' : line[3]},
    'engine room': {'name': 'engine room', 'roomchoice': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[4]'},
    'deck': {'name': 'deck', 'roomchoice': ['captains quarters', 'sleeping quarters'], 'item': '[TEXT]', 'desc' : 'line[5]'}
}
commands = {
    ('pickup','pick-up','take','get','grab'):'take',
    ('use','apply','operate'):'use',
    ('go','walk','run','leave','climb'):'go',
    ('look','inspect','view','l'):'look'
}

cur_location = rooms['captains quarters']

def parse_input(text_input):
    words = text_input.split(' ')
    helper_commands = ['at','to','in','through','by','the','and','but','inside','toward']
    for word in words[:]:
        if word in helper_commands: 
            words.remove(word)
    for roomcheck in rooms:
        if roomcheck in text_input:
            r = True
            room_output = roomcheck
            break
    for command in commands:
        if words[0] in command:
            output = f'{commands[command]} {" ".join(words[1:])}'
            if r:
                return commands[command], room_output
            print(output)
            return output, None


def pickup_item():
    cur_item = rooms[cur_location['item']]
    if cur_location['item'] == 'nothing':
        print(f"You've already picked up {cur_item}.")
        return
    gamestate['inventory'].append(cur_item)
    print(f"You picked up the {cur_item}.")
    cur_location['item'] = 'nothing'

def use_item(gamestate):
    if gamestate['current location'] == 'deck':
        gamestate['inventory'].remove('crowbar')
        print(line[...])

def goto_location(room_output):
    if room_output in rooms[cur_location['roomchoice']]:
        cur_location = rooms[room_output]
        print(cur_location)
        return cur_location
    else:
        print('You cannot go to that room from here')








#–––––––––––––––––––––––––––––––––––––––––––––––––––
# 
# Bugs: 
# - Om man tar upp ett item och sedan använder det kommer det fortfarande finnas kvar.        
#   - lösn: remove:a från commands?
# - Endast 'use', 'go to' och 'pick up' fungerar.
#    commands = ['up', 'down', 'outside', 'inside' 'inventory', 'key', 'toolbox', 'crowbar', 'fuse', 'food']
