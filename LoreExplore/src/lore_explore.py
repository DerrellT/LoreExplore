import json # loads json 

with open('LoreExplore/data/characters.json') as f: #with .... as f is good cause it does auto cleanup, safe and cleaner aka no random files floating around
    chars = json.load(f) #json.load(f) converts json into a python object
    #chars (was data) is now a dictionary with a key 'characters' pointing to my list of dictionaries
with open('LoreExplore/data/regions.json') as f: 
     regs = json.load(f)
with open('LoreExplore/data/vanguard.json') as f: 
     vang = json.load(f)

def main(): #doesnt need parameters, need one main function to take user input and call the other functions if not found in one.
    
    user_input = input("Enter a character, region or vangaurd: ").lower()#moved lower here
    
    result = search_characters(user_input)# checks character data first if result is none goes to next function
    if result:
        display_character(result) #goes to next function
        return
    
    result = search_region(user_input)
    if result:
        display_region(result)
        return
    
    result = search_vanguards(user_input)
    if result: 
        display_vanguard(result)
        return
    
    print("Not Found")
    
def search_characters(name): #searches name through dictionary
    for character in chars["characters"]:
        if character["name"].lower() == name:
            return character #returns entire dictionary
    return None


def search_region(name):
    for region in regs["regions"]:
        if region["region_name"].lower() == name:
            return region
    return None


def search_vanguards(name):
    for vanguard in vang["vanguards"]:
        if vanguard["vanguard_name"].lower() == name:
            return vanguard
    return None



def display_character(character): #gets to this function and formats traits so no seen brackets
    print(f"Name: {character.get('name')}")    
    traits = character.get("traits", []) #get fetches everything associated with traits if there is any otherwise nothing
    if traits:
        print("Traits: ")
        for trait in traits: #goes through list and displays each trait
            print(f"- {trait}") #displays each trait with a bracket as a list


def display_region(region):
    print(f"Region: {region.get('region_name')}")
    descriptions = region.get("descriptions", [])
    if descriptions:
        print("Descriptions: ")
        for descriptions in descriptions:
            print(f"- {descriptions}")
 

def display_vanguard(vanguard):
    print(f"Vanguard: {vanguard.get('vanguard_name')}")
    roles = vanguard.get("roles", [])
    if roles:
        print("Roles: ")
        for role in roles:
            print(f"- {role}")

main() #call my function or else it wont even show up

