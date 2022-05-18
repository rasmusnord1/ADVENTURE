from LineJoin import *
from UsageError import *
from End import *

file = open('Text_support.txt')
line = file.readlines()


def look_check(gamestate):

    user_input = gamestate['current user input']

    lookat_input = user_input.split()[1:]
    lookat_input_text = " ".join(lookat_input)

    itemlocation_check = lookat_input_text in gamestate['current location']['lookat']

    lookat_object_list = {'desk': line_join(22), 'papers': line_join(22), 'bed': line_join(24), 'engine': line_join(33), 'fusebox': line_join(35), 'lifeboat': line_join(42)}
    
    if itemlocation_check:

        if lookat_input_text in lookat_object_list:

            input(lookat_object_list[lookat_input_text])
            return 

        elif lookat_input_text == 'corner' and 'crowbar' not in gamestate['items taken']:

            input(line_join(27))
            return 

        elif lookat_input_text == 'bag' and 'key' not in gamestate['items taken']:

            input(line_join(30)) 
            return 

        elif lookat_input_text == 'shipping container':

            if gamestate['shipping container'] == 'closed':
                input(line_join(44))

            elif gamestate['shipping container'] == 'open':
                input(line_join(46))


        elif lookat_input_text == 'locker':

            if gamestate['locker'] == 'closed':
                input(line_join(37))

            elif gamestate['locker'] == 'open' and 'toolbox' not in gamestate['items taken']:
                input(line_join(39))

            else:
                return usage_error()

        elif lookat_input_text == 'radio':

            if gamestate['electricity'] == 'off':
                input(line_join(20))

            elif gamestate['electricity'] == 'on':
                end('GOOD')
        
        else:
            return usage_error()
    else:
        return usage_error()
    return