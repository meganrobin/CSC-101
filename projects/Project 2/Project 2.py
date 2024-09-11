import random

 #Message to introduce the player to the game#
print("\33[34mAh there's the Hero, and not a momment too soon! The once utopian lands of our precious kingdom have been infested with terrible monsters, and you are the only one with the ability to banish them for good! Each monster has a special weakness against a specific weapon, and it's up to you to figure out which one defeats each goulish beast. Quick, I see one approaching now!\33[37m")

#Assigns a random amount of usages (between 1 and 4) to each weapon variable#
#Global variables are used for the weapon variables so that their int values can be easily decreased within the outcome() function each time the player uses a weapon#
global int_sword
int_sword = random.randint(1,4)
global int_arrow
int_arrow = random.randint(1,4)
global int_magic
int_magic = random.randint(1,4)
global int_hammer
int_hammer = random.randint(1,4)

global total_monsters
total_monsters = 0

#Initialize dictionary containing the monster names as keys and the corresponding weapons that defeat each monster as the values#
monsters = {
"\33[96mDragon\33[37m": "int_arrow",
"\33[32mZombie\33[37m": "int_sword",
"\33[35mGhost\33[37m": "int_magic",
"\33[33mMinotaur\33[37m": "int_hammer"
}

def monster_encounter(): #picks a random monster, tells the player which monster has appeared, and calls the player_input function#
    current_monster = "" #holding variable for a random monster from the 4 monster options#
    random_index = random.randint(0,3) #sets random_index equal to a random int between 0 and 3#
    for i, key in enumerate(monsters.keys()): #finds the key in monsters[] with the same index as the number random_index was set to#
        if i == random_index:
            current_monster = key #sets current_monster equal to a string containing the current monster's name#

    print(f"\nA {current_monster} appears!")#tells the player which monster has appeared#
    player_input(current_monster)#calls the player_input function with the current monster as the argument#

def player_input(monster): 
    #tells the player how many uses of each weapon they have left#
    print("\nHero's Arsenal:")
    print(f"1. sword  ({int_sword} uses left)")
    print(f"2. arrow  ({int_arrow} uses left)")
    print(f"3. magic  ({int_magic} uses left)")
    print(f"4. hammer ({int_hammer} uses left)")
    print("\nEnter the number of the weapon to use:")
    
    weapon_input = input() #sets weapon_input equal to the number the player enters#
   
    if weapon_input == "1": #finds which weapon the player picked#
        if int_sword > 0: #checks if the weapon still has uses keft#
            outcome(monster,"int_sword") #if there are weapon uses left, calls outcome() with arguments - string name of the monster, amount of uses of the selected weapon, and string containing the name of the weapon#
        else:
            print("You don't have any uses of the sword left! Try another weapon.") #if there are no weapon uses left, notifies player and recalls the player_input() function#
            player_input(monster)
    elif weapon_input == "2":
        if int_arrow > 0:
            outcome(monster,"int_arrow")
        else:
            print("You don't have any uses of the arrow left! Try another weapon.")
            player_input(monster)
    elif weapon_input == "3":
        if int_magic > 0:
            outcome(monster,"int_magic")
        else:
            print("You don't have any uses of magic left! Try another weapon.")
            player_input(monster)
    elif weapon_input == "4":
        if int_hammer > 0:
            outcome(monster,"int_hammer")
        else:
            print("You don't have any uses of the hammer left! Try another weapon.")
            player_input(monster)
    else:
        print("Please type the number 1, 2, 3, or 4.") #notifies the player and recalls player_input if the player types something other than the number 1, 2, 3, or 4#
        player_input(monster)

def outcome(monster,weapon_value): #called when the player enters the number of the weapon they want to use# #Checks if the player has enough usages to defeat the monster, and if the weapon they chose matches the monster#
    for key in monsters.keys():
        if key == monster: #finds the correct monster in the dictionary#
            if monsters[key] == weapon_value: #checks if it's the correct weapon for the monster, and prints the winning message if it is#
                print(f"\033[92mYou defeated the {monster} with {weapon_value[4:]}! Press enter to continue on your journey.\33[37m")
                input()

                global total_monsters
                total_monsters += 1 #increases the total amount of monsters defeated count#

                #decreases the global variable that corresponds to the current selected weapon by 1#
                if weapon_value == "int_sword": 
                    global int_sword
                    int_sword -= 1
                if weapon_value == "int_arrow":
                    global int_arrow
                    int_arrow -= 1
                if weapon_value == "int_magic":
                    global int_magic
                    int_magic -= 1
                if weapon_value == "int_hammer":
                    global int_hammer
                    int_hammer -= 1
                monster_encounter()#calls the monster_encounter() function again to set up another monster encounter, since the player successfully defeated the current monster#
            elif monsters[key] != weapon_value: #If it's NOT the correct weapon for the monster, gives the player an end game message, then gives the player the final amount of monsters defeated#
                print(f"\33[31mThe {monster} \33[31mis immune to {weapon_value[4:]}. You were defeated.\33[37m")
                print(f"You defeated \33[34m{total_monsters}\33[37m total monsters. Nice work!")

monster_encounter()#called to start up the very first monster encounter#