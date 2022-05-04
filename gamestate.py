file = open('Text_support.txt')
line = file.readlines()

gamestate = {}
gamestate['inventory'] = []
gamestate['current location'] = 'kitchen'

rooms = {
    'captains quarters': {'name': 'captains quarters', 'down': 'deck', 'item': 'crowbar', 'desc' : 'line[10]'},
    'kitchen': {'name': 'kitchen', 'down': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[2]'},
    'sleeping quarters': {'name': 'sleeping quarters', 'up': 'kitchen', 'down': 'engine room','outside': 'deck', 'item': '[TEXT]', 'desc' : line[3]},
    'engine room': {'name': 'engine room', 'up': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[4]'},
    'deck': {'name': 'deck', 'inside1': 'captains quarters', 'inside2': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[5]'}
}
commands = {
    ('pickup','pick-up','take','get','grab'):'take',
    ('use','apply','operate'):'use',
    ('go','walk','run','leave','climb'):'go',
    ('look','inspect','view','l'):'look'
}




cur_location = rooms['captains quarters']


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
        cur_location['item'] = room_output

for roomcheck in rooms:

            r = True
            room_output = roomcheck

commands['take item'] = {
    'perform': pickup_item
}
commands['use item'] = {
    'perform': use_item
}
commands['go'] = {
    'perform': goto_location(room_output)
}
#}




#–––––––––––––––––––––––––––––––––––––––––––––––––––
# 
# Bugs: 
# - Om man tar upp ett item och sedan använder det kommer det fortfarande finnas kvar.        
#   - lösn: remove:a från commands?
# - Endast 'use', 'go to' och 'pick up' fungerar.
#    commands = ['up', 'down', 'outside', 'inside' 'inventory', 'key', 'toolbox', 'crowbar', 'fuse', 'food']
