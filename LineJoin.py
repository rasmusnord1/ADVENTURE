file = open('Text_support.txt')
line = file.readlines()

def line_join(number):

    return f"\n{''.join(line[int(number)])}"