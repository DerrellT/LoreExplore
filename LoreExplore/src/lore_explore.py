import json # loads json 

with open('LoreExplore/data/characters.json') as f: #with .... as f is good cause it does auto cleanup, safe and cleaner aka no random files floating around
    chars = json.load(f) #json.load(f) converts json into a python object
    #chars (was data) is now a dictionary with a key 'characters' pointing to my list of dictionaries
with open('LoreExplore/data/regions.json') as f: 
     regs = json.load(f)
with open('LoreExplore/data/vanguard.json') as f: 
     vang = json.load(f)

def main(): #doesnt need parameters
    user_input = input("Enter a character, region or vangaurd: ")
    result = search_characters(user_input)# the function is search character
    
    if result is None:
        result = search_region(user_input)
    
    if result is None:
         result = search_vanguards(user_input)

    

    print(result)

def search_characters(search_term): # search_terms is the input i cam checking in json data
    search_term = search_term.lower() #takes what the user put to lower case 
    
    for character in chars["characters"]: #loops through each character in the list 
        if character["name"].lower() == search_term:
            return(character["name"]) #if name is found it returns and stops looping
    return None



def search_region(search_term): # search_terms is the input i cam checking in json data
    search_term = search_term.lower() #takes what the user put to lower case 
    
    for region in regs["regions"]: #loops through each character in the list 
        if region["region_name"].lower() == search_term:
            return(region["region_name"]) #if name is found it returns and stops looping
    return None #loop finishes with no matcha and returns none

def search_vanguards(search_term):
    search_term = search_term.lower()
    
    for vanguard in vang["vanguards"]:
      if vanguard["vanguard_name"].lower() == search_term:
           return(vanguard["vanguard_name"])
    return None

main() #call my function or else it wont even show up




 