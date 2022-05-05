# file = open('Text_support.txt')
  
# # read the content of the file opened
# content = file.readlines()
  
# # read 10th line from the file
# print("tenth line")
# print(content[1])



# gamestate = {}
# gamestate["inventory"] = []
# gamestate["current location"] = "kitchen"

# commands = {}

# def can_pickup_crowbar(gamestate):
#     return gamestate["current location"] == "captains quarters"

# def pickup_crowbar(gamestate):
#     gamestate["inventory"].append("crowbar")

# commands["pickup crowbar"] = {
#     "can_perform": can_pickup_crowbar,
#     "perform":pickup_crowbar
# }


# print(commands)

# print(gamestate)
# print(commands["pickup crowbar"]["can_perform"](gamestate)) # True om det går
# commands["pickup crowbar"]["perform"](gamestate)
# print(gamestate)





















# rooms = {
#     'captains quarters': {'name': 'captains quarters', 'roomchoice': 'deck', 'item': 'crowbar', 'desc' : 'line[10]'},
#     'kitchen': {'name': 'kitchen', 'roomchoice': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[2]'},
#     'sleeping quarters': {'name': 'sleeping quarters', 'roomchoice': ['kitchen','engine room', 'deck'], 'item': '[TEXT]', 'desc' : 'line[3]'},
#     'engine room': {'name': 'engine room', 'roomchoice': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[4]'},
#     'deck': {'name': 'deck', 'roomchoice': ['captains quarters', 'sleeping quarters'], 'item': '[TEXT]', 'desc' : 'line[5]'}
# }

# cur_location = rooms['captains quarters']


# print('{}'.format(cur_location['item']))


#Gamla rooms-systemet, utan roomchoice. 
# rooms = {
#     'captains quarters': {'name': 'captains quarters', 'down': 'deck', 'item': 'crowbar', 'desc' : 'line[10]'},
#     'kitchen': {'name': 'kitchen', 'down': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[2]'},
#     'sleeping quarters': {'name': 'sleeping quarters', 'up': 'kitchen', 'down': 'engine room','outside': 'deck', 'item': '[TEXT]', 'desc' : line[3]},
#     'engine room': {'name': 'engine room', 'up': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[4]'},
#     'deck': {'name': 'deck', 'inside1': 'captains quarters', 'inside2': 'sleeping quarters', 'item': '[TEXT]', 'desc' : 'line[5]'}




        #     command = input('\nWhat would you like to do?').strip()  # Get player command input
    #     if command in commands:

    #        if command in cur_location:
    #             cur_location = rooms[cur_location[command]]

    #         if command in 'bing':
    #             inventory.append(rooms[cur_location[command]])

    #     elif command.lower() == 'quit':  
    #         print('You quit the game.')
    #         break
    # else:
    #          if invalid command is given
    #         print('The loneliness of this place must be getting to you. Please try something else.')
    # print()