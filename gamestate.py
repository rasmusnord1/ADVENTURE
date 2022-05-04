
gamestate = {}
gamestate["inventory"] = []
gamestate["current location"] = "kitchen"

commands = {}

#def can_pickup_crowbar(gamestate):
#    return gamestate["current location"] == "kitchen"

#def pickup_crowbar(gamestate):
#    if can_pickup_crowbar(gamestate):
#        gamestate["inventory"].append("crowbar")
 


def pickup_crowbar(gamestate):
    if gamestate["current location"] == "kitchen":
        gamestate["inventory"].append("crowbar")
        print("You picked up the crowbar.")

def use_crowbar(gamestate):
    if gamestate["current location"] == "deck":
        gamestate["inventory"].pop("crowbar")
        print(line[NUMMERSIFFRA])


commands["pick up crowbar"] = {
    "perform": pickup_crowbar
}
commands["use crowbar"] = {
    "perform": pickup_crowbar
}


#–––––––––––––––––––––––––––––––––––––––––––––––––––
# 
# Bugs: 
# - Om man tar upp ett item och sedan använder det kommer det fortfarande finnas kvar.        
#   - lösn: pop:a från commands
# - Endast 'use' och 'pick up' fungerar. 