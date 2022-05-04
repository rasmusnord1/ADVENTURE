file = open('Text_support.txt')
  
# read the content of the file opened
content = file.readlines()
  
# read 10th line from the file
print("tenth line")
print(content[1])


rooms = {
    'captains quarters': {'name': 'captains quarters', 'down': 'deck', 'item': 'crowbar', 'desc' : 'line[10]'},
    'kitchen': {'name': 'kitchen', 'down': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[2]'},
    'sleeping quarters': {'name': 'sleeping quarters', 'up': 'kitchen', 'down': 'engine room','outside': 'deck', 'item': '[TEXT]', 'desc' : line[3]},
    'engine room': {'name': 'engine room', 'up': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[4]'},
    'deck': {'name': 'deck', 'inside1': 'captains quarters', 'inside2': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[5]'}