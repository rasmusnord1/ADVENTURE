# file = open('Text_support.txt')
# line = file.readlines()

# text_input = 'go'
# cmd_options = {}



# cmd_options['go'] = {
#             'perform': print("shit go")
#         }
# cmd_options['use item'] = {
#             'perform': print('shit went')
#         }

# cmd_options['goto location'] = {
#     'perform': print('shit gone')
#         }

# print('go' in cmd_options)

# list = ['Hi' , 'hello', 'at', 'this', 'there', 'from']
# list2 = ['shit', 'also', 'poop']

# input = 'hello'
# if input in list:
#     index = list.index(input)
#     print(index)
#     print(list2[index])

# cmd_options['go'] = {
#             'perform': print("shit go")
#         }
# cmd_options['use item'] = {
#             'perform': print('shit went')
#         }

# cmd_options['goto location'] = {
#     'perform': print('shit gone')
#         }


def item(input):
    if input == 'crowbar':
        print('shit cunt it worked')

file = open('Text_support.txt')
line = file.readlines()

def line_join(number):
    return f"\n{''.join(line[int(number)])}"

def use_item_success(item_used):
    # item_use_list = {}
    # item_use_list['crowbar'] = {
    #     'perform': line_join(20),
    #     'also_perform': item(item_used)
    # }
    
    item_use_list = {'crowbar': line_join(20), 'fuse': line_join(22), 'papers': line_join(22), 'bed': line_join(24)}
    input(item_use_list[item_used])
    return

use_item_success('crowbar')




#–––––––––––––––––––––––––––––––––––––––––––––––––––
# 
# Bugs: 
# - Om man tar upp ett item och sedan använder det kommer det fortfarande finnas kvar.        
#   - lösn: remove:a från commands?
# - Endast 'use', 'go to' och 'pick up' fungerar.
#    commands = ['up', 'down', 'outside', 'inside' 'inventory', 'key', 'toolbox', 'crowbar', 'fuse', 'food']
