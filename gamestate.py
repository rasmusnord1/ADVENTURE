# file = open('Text_support.txt')
# line = file.readlines()

text_input = 'go'
cmd_options = {'go': print("user_input")}        
if text_input in cmd_options:
    cmd_options[text_input]

#–––––––––––––––––––––––––––––––––––––––––––––––––––
# 
# Bugs: 
# - Om man tar upp ett item och sedan använder det kommer det fortfarande finnas kvar.        
#   - lösn: remove:a från commands?
# - Endast 'use', 'go to' och 'pick up' fungerar.
#    commands = ['up', 'down', 'outside', 'inside' 'inventory', 'key', 'toolbox', 'crowbar', 'fuse', 'food']
