
from LineJoin import *
from End import *

file = open('Text_support.txt')
line = file.readlines()


def ending_check(gamestate):

    user_input = gamestate['current user input']

    if 'use lifeboat' in user_input: 

        if gamestate['current location']['name'] == 'deck': 
            return end('BAD')

    elif 'use radio' in user_input and gamestate['current location']['name'] == 'captains quarters':

        if gamestate['electricity'] == 'off':
            input(line_join(20))
            return 

        elif gamestate['electricity'] == 'on':
            return end('GOOD')