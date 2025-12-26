import json # loads json 
#TKINTER
#def function
with open('LoreExplore/data/characters.json') as f: #with .... as f is good cause it does auto cleanup, safe and cleaner aka no random files floating around
    chars = json.load(f) #json.load(f) converts json into a python object
    #data is now a dictionary with a key 'characters' pointing to my list of dictionaries
with open('LoreExplore/data/regions.json') as f: 
     regs = json.load(f)
with open('LoreExplore/data/vanguard.json') as f: 
     vang = json.load(f)


for character in chars["characters"]: #loops through each character in th elist and prints the name field
    print(character["name"])

for region in regs["regions"]:
    print(region["region_name"])

for vanguard in vang["vanguards"]:
    print(vanguard["vanguard_name"])