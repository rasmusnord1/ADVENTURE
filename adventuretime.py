from gamestate import *
#import time
#- för att använda time.sleep(x)
file = open('Text_support.txt')
line = file.readlines()

#Text_support = "Text_support.txt"

#with open(Text_support) as f:
#    line = f.readlines()
# How to read: https://www.pythontutorial.net/python-basics/python-read-text-file/




#input("\n\n>> ")


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
                return f'{commands[command]}', room_output
            print(output)
            return output








def main(): #kanske ta bort funktionen
#    main_menu()
    print(f'\n\n{line[0]}, ')


    # current location 
    cur_location = 'captains quarters'
N = True
#def main_game():
while N == True:
#        print('You are in the {}.'.format(cur_location['name'], ))  # Print current location
#        print('This room contains {}.'.format(cur_location['item'], ))  # Print the item in the locations, BEHÖVS NOG INTE
        print(f'\n\n{"".join(line[1:4])}')

        text_output, room_output = parse_input(input('\n\nWhat would you like to do?\n>> '))

        
        N = False




#        command = input('\nWhat would you like to do?').strip()  # Get player command input
#        if command in commands:
#
 #           if command in cur_location:
  #              cur_location = rooms[cur_location[command]]
#
 #           if command in 'bing':
  #              inventory.append(rooms[cur_location[command]])
#
 #       elif command.lower() == 'quit':  
  #          print('You quit the game.')
   #         break
    #else:
            # if invalid command is given
 #           print('The loneliness of this place must be getting to you. Please try something else.')
#    print()

#print(main())
