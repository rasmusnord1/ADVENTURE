file = open('Text_support.txt')
line = file.readlines()

def inventory_check(gamestate, main):

    if gamestate['inventory'] == []:
        input('\nYou have nothing in your inventory.')

    else:
        inventory_text = (', ').join(gamestate['inventory'])
        input(f"\nThe following things are in your inventory: \n{inventory_text}")
        
    return main()