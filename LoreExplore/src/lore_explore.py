import json # loads json 

with open('LoreExplore/data/characters.json') as f: #with .... as f is good cause it does auto cleanup, safe and cleaner aka no random files floating around
    chars = json.load(f) #json.load(f) converts json into a python object
    #chars (was data) is now a dictionary with a key 'characters' pointing to my list of dictionaries
with open('LoreExplore/data/regions.json') as f: 
     regs = json.load(f)
with open('LoreExplore/data/vanguard.json') as f: 
     vang = json.load(f)



def search_characters(search_term):
    search_term = search_term.lower() #case sensitive 
    
    for character in chars["characters"]: #loops through each character in th elist and prints the name field
        if character["name"].lower() == search_term:
            return(character["name"])
    return None
user_input = input("Enter a character name: ")
result = search_characters(user_input) # the function is search characters
print(result)

# def search_regions
  #  for region in regs["regions"]:
  #  
  #      if search_term in regs[region]:
  #          return(region["region_name"])
  #      return
# def search_vanguards
 # for vanguard in vang["vanguards"]:
 #      
 #      if search_term in vang[vanguard]:
 #           return(vanguard["vanguard_name"])
 #      return


 