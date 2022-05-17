command_switch_list = {
    ('pickup','pick-up','take','get','grab','t'):'take',
    ('use','apply','operate','u'):'use',
    ('go','walk','run','leave','climb','g'):'go',
    ('look','inspect','investigate','view','l'):'look',
    ('help','h','hjälp',):'help',
    ('inventory', 'i'):'inventory'
}

helper_commands = ['at','to','in','through','by','the','and','but','toward','outside','inside','down','up','metal']


def parse_input(text_input):

    words = text_input.split(' ')

    for word in words[:]:

        if word in helper_commands: 
            words.remove(word)

    for command_switch in command_switch_list:

        if words[0] in command_switch:
            parsed_text_input = f'{command_switch_list[command_switch]} {" ".join(words[1:])}' 

            return parsed_text_input
