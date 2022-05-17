file = open('Text_support.txt')
line = file.readlines()

def end(ending_type, line_join):
    if ending_type == 'BAD':
        input(line_join(60))

    elif ending_type == 'NEUTRAL':
        input(line_join(62))

    elif ending_type == 'GOOD':
        input(line_join(64))
        
    return quit()