

def parse_input(text_input):
    print('bing')
    words = text_input.split(' ')
    helper_commands = ['at','to','in','through','by','the','and','but','toward','outside','inside','down','up']
    for word in words[:]:
        if word in helper_commands: 
            words.remove(word)
    for command in command_switch:
        if words[0] in command:
            user_input = f'{command_switch[command]} {" ".join(words[1:])}' 
            #rest_input = " ".join(words[1:])
            print(user_input)
            return user_input#, rest_input # kanske användbart.
