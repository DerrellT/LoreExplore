import json #json 
#TKINTER
#open them
#def function
#search them
#display results
with open('/Users/derrellturner/projects/LoreExplore/data/characters.json') as f:
    data = json.load(f)
#def()

for character in data["characters"]:
    print(character["name"])