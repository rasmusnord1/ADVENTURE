def death(user_input):
    if 'use lifeboat' in user_input: 
        if gamestate['current location']['name'] == 'deck': 
            return end('BAD')
        return usage_error()