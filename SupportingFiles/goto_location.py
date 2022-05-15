def can_goto_location(user_input):
    words = user_input.split()
    if words[0] == 'go':
        input_in_roomchoice_check = ' '.join(words[1:]) in gamestate['current location']['roomchoice']
        return input_in_roomchoice_check # Trash namn

def goto_location(user_input):
    if can_goto_location(user_input):
        words = user_input.split()
        gamestate['current location'] = rooms[' '.join(words[1:])]
        input(f"\nYou walk to the {gamestate['current location']['name']}") 
        return main()
    return usage_error()