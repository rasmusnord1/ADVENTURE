from gamestate import *
#import time
#- för att använda time.sleep(x)
file = open('Text_support.txt')
line = file.readlines()

#Text_support = "Text_support.txt"

#with open(Text_support) as f:
#    line = f.readlines()
# How to read: https://www.pythontutorial.net/python-basics/python-read-text-file/






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
        input(f"\n\n{''.join(line[1:4])} \nPress enter to continue.")
        
        print('\n'*7 + f"You are in the {(cur_location['name'])}.\n{''.join(line[8])}")
        text_output, room_output = parse_input(input('\n\nWhat would you like to do?\n>> '))
        
        
        N = False

commands['take item'] = {
    'perform': pickup_item
}
commands['use item'] = {
    'perform': use_item
}
commands['go', room_output] = {
    'perform': goto_location(room_output)
}





#print(main())
