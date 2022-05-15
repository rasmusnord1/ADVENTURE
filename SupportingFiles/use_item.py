def use_item_success(item_used):
    item_text_list = {'crowbar': line_join(20), 'fuse': line_join(22), 'papers': line_join(22), 'bed': line_join(24)}
    item_action_list = ['fuse','toolbox', 'key']
    
    input(item_text_list[item_used]) # Tror nog allt måste vara if-satser, då det inte går att appenda typ toolbox från input "key" i dictionary
    if item_used in item_action_list:
        if item_used == 'fuse':
            return main()
        elif item_used == 'key':
            gamestate['inventory'].append('toolbox')
            gamestate['items taken'].append('toolbox')
            input(f"\nYou picked up the toolbox.")

    return main()

def use_item(user_input):
    death(user_input)
    words = user_input.split()
    if len(words) == 1:
        return usage_error()
    item_used_from_input = words[1]
    object_used_on_from_input = (' ').join(words[3:])
    
    # print("Following statements:\nwords[1] in gamestate['current location']['useitem']\nitem_index = gamestate['current location']['useitem'].index(words[1])\nwords[3] == gamestate['current location']['use_item_on'][item_index]\n")
    # print(words[1] in gamestate['current location']['useitem'])
    # item_index = gamestate['current location']['useitem'].index(words[1])
    # print(item_index)
    # print("gamestate: "+gamestate['current location']['use_item_on'][item_index])
    # print("from input: "+ (' ').join(words[3:]))
    # print((' ').join(words[3:]) == gamestate['current location']['use_item_on'][item_index])

    if words[1] in gamestate['inventory']:
        if 'use' and 'on' in words:
            if item_used_from_input in gamestate['current location']['useitem']:
                item_object_combination_check = gamestate['current location']['useitem'].index(item_used_from_input)
                if object_used_on_from_input == gamestate['current location']['use_item_on'][item_object_combination_check]:
                    input(f"\nYou succesfully used your {item_used_from_input} on the {object_used_on_from_input}.")
                    gamestate['inventory'].remove(item_used_from_input)
                    use_item_success(item_used_from_input)
                    return main()
                input("\nNothing happened.")
                return main()
            input("\nYou cannot use that item here.")
            return main()
        input("\nYou have to specify what to use the item on.")
        return main()
    input("\nYou don't have that item in your inventory.")
    return main()