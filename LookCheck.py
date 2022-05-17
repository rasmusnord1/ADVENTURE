file = open('Text_support.txt')
line = file.readlines()

import LineJoin
import UsageError

def look_check(gamestate, main):

    user_input = gamestate['current user input']

    lookat_input = user_input.split()[1:]
    lookat_input_text = " ".join(lookat_input)

    itemlocation_check = lookat_input_text in gamestate['current location']['lookat']

    lookat_object_list = {'desk': LineJoin(22), 'papers': LineJoin(22), 'bed': LineJoin(24), 'corner': LineJoin(27), 'engine': LineJoin(33), 'fusebox': LineJoin(35), 'lifeboat': LineJoin(42)}
    
    if itemlocation_check:

        if lookat_input_text in lookat_object_list:

            input(lookat_object_list[lookat_input_text])
            return main()

        elif lookat_input_text == 'corner' and 'crowbar' not in gamestate['items taken']:

            input(LineJoin(27))
            return main()

        elif lookat_input_text == 'bag' and 'key' not in gamestate['items taken']:

            input(LineJoin(30)) 
            return main()

        elif lookat_input_text == 'shipping container':

            if gamestate['shipping container'] == 'closed':
                input(LineJoin(44))

            elif gamestate['shipping container'] == 'open':
                input(LineJoin(46))


        elif lookat_input_text == 'locker':

            if gamestate['locker'] == 'closed':
                input(LineJoin(37))

            elif gamestate['locker'] == 'open' and 'toolbox' not in gamestate['items taken']:
                input(LineJoin(39))

            else:
                return UsageError(main)

        elif lookat_input_text == 'radio':

            if gamestate['electricity'] == 'off':
                input(LineJoin(20))

            elif gamestate['electricity'] == 'on':
                end('GOOD')
        
        else:
            return UsageError(main)
    else:
        return UsageError(main)
    return main()