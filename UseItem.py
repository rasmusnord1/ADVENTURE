file = open('Text_support.txt')
line = file.readlines()

import LineJoin

def use_item_success(item_used, gamestate):

    if item_used == 'key':

        gamestate['current location']['item'].append('toolbox')
        gamestate['locker'] = 'open'

        input(LineJoin(50))

    elif item_used == 'crowbar':

        gamestate['current location']['item'].append('fuse')
        gamestate['shipping container'] = 'open'

        input(LineJoin(54))

    elif item_used == 'fuse':

        gamestate['electricity'] = 'on'

        input(LineJoin(56))
        
    elif item_used == 'toolbox':

        input(LineJoin(52))

        end('NEUTRAL')

    return main()



def use_item(gamestate, line_join, usage_error, main):

    user_input = gamestate['current user input']


    ending_check(gamestate, line_join, main)
    words = user_input.split()

    if len(words) == 1:
        return usage_error()
        
    item_used_from_input = words[1]
    object_used_on_from_input = (' ').join(words[3:])
    
    if words[1] in gamestate['inventory']:
        if 'use' and 'on' in words:

            if item_used_from_input in gamestate['current location']['useitem']:

                item_object_combination_check = gamestate['current location']['useitem'].index(item_used_from_input)

                if object_used_on_from_input == gamestate['current location']['use_item_on'][item_object_combination_check]:

                    input(f"\nYou succesfully used your {item_used_from_input} on the {object_used_on_from_input}.")
                    gamestate['inventory'].remove(item_used_from_input)

                    use_item_success(item_used_from_input, gamestate)

                    return main()

                input("\nNothing happened.")
                return main()

            input("\nYou cannot use that item here.")
            return main()

        input("\nYou have to specify what to use the item on.")
        return main()

    input("\nYou don't have that item in your inventory.")
    return main()


    