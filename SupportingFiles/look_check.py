def look_check(user_input):
    lookat_input = user_input.split()[1:]
    lookat_input_text = "".join(lookat_input)
    itemlocation_check = lookat_input_text in gamestate['current location']['lookat']
    
    lookat_list = {'radio': line_join(20), 'desk': line_join(22), 'papers': line_join(22), 'bed': line_join(24)}

    if itemlocation_check:
        if lookat_input_text in lookat_list:
            input(lookat_list[lookat_input_text])
            return main()

        # else:
        #     item_switch_lookat_list = {'corner': 'crowbar', 'bag': 'key'}
        #     item_action_list = 
        #     for command in item_switch_lookat_list:
        #         if lookat_input_text in command:
        #             user_input = item_switch_lookat_list[command]

        elif lookat_input_text == 'corner' and 'crowbar' not in gamestate['items taken']:
            input(line_join(27))
            return main()
        elif lookat_input_text == 'bag' and 'key' not in gamestate['items taken']:
            input(line_join) # NOT DONE
            return main()

    #!
    # Alternativt istället för if-satser att använda sig utav command_switch-liknande
    # - Kanske är långsammare?
    
    return usage_error()