file = open('Text_support.txt')
line = file.readlines()

import LineJoin
import End

def ending_check(gamestate, main):

    user_input = gamestate['current user input']

    if 'use lifeboat' in user_input: 

        if gamestate['current location']['name'] == 'deck': 
            return End('BAD', LineJoin)

    elif 'use radio' in user_input and gamestate['current location']['name'] == 'captains quarters':

        if gamestate['electricity'] == 'off':
            input(LineJoin(20))
            return main()

        elif gamestate['electricity'] == 'on':
            return End('GOOD', LineJoin)

# testa123