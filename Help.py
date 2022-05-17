file = open('Text_support.txt')
line = file.readlines()

def help(preventTypeError, main):

    input("\n"*3 + ''.join(line[68:81]))


    return main()

