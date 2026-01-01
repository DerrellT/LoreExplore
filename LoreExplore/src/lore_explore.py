import json # loads json 

def check_json_files():
    chars = regs = vang = None # set to none then as data gets added I see
    try : 
        with open('LoreExplore/data/characters.json') as f:
            chars = json.load(f)
    
    except FileNotFoundError:
        print("Missing Characters JSON File")
    except json.JSONDecodeError:
        print("Characters JSON is invalid")
    
    try :
        with open('LoreExplore/data/regionsjson') as f: 
            regs = json.load(f)
    except FileNotFoundError:
        print("Missing Regions JSON File")
    except json.JSONDecodeError:
        print("Regions JSON is invalid")
       
    try :
        with open('LoreExplore/data/vanguard.json') as f: 
            vang = json.load(f)
    except FileNotFoundError:
        print("Missing Vanguard JSON File")
    except json.JSONDecodeError:
        print("Vanguard JSON is invalid")
            
    return chars, regs, vang #to see which file didnt load

def main(): #doesnt need parameters, need one main function to take user input and call the other functions if not found in one.
    chars, regs, vang = check_json_files()
    
    if chars is None:
        print("Characters data missing. Exiting.")
        return
    if regs is None:
        print("Regions data missing. Exiting.")
        return
    if vang is None:
        print("Vanguards data missing. Exiting.")
        return
    
    print("------Characters------ ") #helps user see then seperated sections
    
    for character in chars["characters"]: #goes through each character
        print(character.get("name")) #searches chars and gets each key value which is the names

    print("------Regions-------- ")      

    for region in regs["regions"]:
           print(region.get("region_name"))

    print("------Vanguards------ ")

    for vanguard in vang["vanguards"]:
        print(vanguard.get("vanguard_name"))
    
    while True:
        found = False 
        user_input = input("Enter a Character, Region or Vangaurd from the list above: ").lower() #moved lower here 

        if user_input == "quit": #added the choice to exit before searching through data
            print("Search ended")
            break #stops program breaks loop
        if user_input == "exit":
            print("Search ended")
            break
    
    
        result = search_characters(user_input, chars) #checks character data first if result is none goes to next function, passes chars
        if result:
            found = True 
            display_character(result) #goes to next function
            
    
        result = search_region(user_input, regs)
        if result:
            found = True
            display_region(result)
            
    
        result = search_vanguards(user_input, vang)
        if result: 
            found = True
            display_vanguard(result)
            

        if not found: #prints below if found remains false
            print("Not Found.")
            print("Try again.")


    

    
    
def search_characters(name, chars): #searches name through dictionary, passes chars parameter from check files
    for character in chars["characters"]:
        if character["name"].lower() == name:
            return character #returns entire dictionary
    return None


def search_region(name, regs):
    for region in regs["regions"]:
        if region["region_name"].lower() == name:
            return region
    return None


def search_vanguards(name, vang):
    for vanguard in vang["vanguards"]:
        if vanguard["vanguard_name"].lower() == name:
            return vanguard
    return None



def display_character(character): #gets to this function and formats traits so no seen brackets
    print(f"Name: {character.get('name')}")    
    traits = character.get("traits", []) #get fetches everything associated with traits if there is any otherwise nothing. dictionary.get(keyname)
    if traits:
        print("Traits: ")
        for trait in traits: #goes through list and displays each trait
            print(f"- {trait}") #displays each trait with a bracket as a list


def display_region(region):
    print(f"Region: {region.get('region_name')}")
    descriptions = region.get("descriptions", [])
    if descriptions:
        print("Descriptions: ")
        for descr in descriptions:
            print(f"- {descr}")
 

def display_vanguard(vanguard):
    print(f"Vanguard: {vanguard.get('vanguard_name')}")
    roles = vanguard.get("roles", [])
    if roles:
        print("Roles: ")
        for role in roles:
            print(f"- {role}")


main() #call my function or else it wont even show up

