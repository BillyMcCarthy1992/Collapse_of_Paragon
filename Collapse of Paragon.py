import random

vale = "\U0001F9D9"
smiling_demon = "\U0001F608"
frowning_demon = "\U0001F47F"
skull = "\U0001F480"
heart = "\U0001F496"
One_hundred = "\U0001F4AF"
speech = "\U0001F4AC"
run_away = "\U0001F4A8"
mageicon = "\U0001F9D9"
warrioricon = "\U0001F9DD"
tree_one = "\U0001F332"
tree_two = "\U0001F333"
mushroom = "\U0001F344"
classical_building = "\U0001F3DB"
hut = "\U0001F6D6"
castle = "\U0001F3F0"
moon = "\U0001F319"
planet = "\U0001FA90"
star =  "\U0001F31F"
lightning = "\U0001F329"
tornado = "\U0001F32A"
fire = "\U0001F525"
water = "\U0001F4A7"
wave = "\U0001F30A"
scrollfrag = "\U0001F4DC"
dice = "\U0001F3B2"
gem = "\U0001F48E"
moneybag = "\U0001F4B0"
coin = "\U0001FA99"
locked = "\U0001F512"
unlocked =  "\U0001F513"
key = "\U0001F5DD"
axe = "\U0001FA93"
sword = "\U0001F5E1"
bomb = "\U0001F4A3"
bow = "\U0001F3F9"
shield = "\U0001F6E1"
blooddrop = "\U0001FA78"
headstone = "\U0001FAA6"
sleepface = "\U0001F634"
injured = "\U0001F915"
uppercut = "\U0001F44A"
potion = "\U0001F37E"
speech = "\U0001F4AC"
bolt = "\U0001F4AB"
smash = "\U0001F4A5"

class warrior:
    def __init__(self, name, health, physical_strength, magical_strength, speed, attacks):
        self.name = name 
        self.health = health
        self.physical_strangth = physical_strength 
        self.magical_strength = magical_strength
        self.speed = speed
        self.attacks = attacks


class mage:
    def __init__(self, name, health, physical_strength, magical_strength, speed, attacks):
        self.name = name 
        self.health = health
        self.physical_strangth = physical_strength 
        self.magical_strength = magical_strength
        self.speed = speed
        self.attacks = attacks


class demon:
    def __init__(self, name, health, physical_strength, magical_strength, speed, attacks):
        self.name = name 
        self.health = health
        self.physical_strangth = physical_strength 
        self.magical_strength = magical_strength
        self.speed = speed
        self.attacks = attacks


def use_potion(character):
    for i in inventory:
        if i["item"]["name"] == "potion":
            if character["max_health"] - character["health"] > 5:
                character["health"] += 5
            else: 
                character["health"] = character["max_health"]
            i["number"] -= 1
            if i["number"] == 0:
                inventory.remove({"item": Potion, "number": 0})
            print(f"\n\033[3m***{Name} drank the {potion}. Their health increased!***\033[0m") 
            print(heart * 5)
            print(f"\033[3m***Their health increased!***\033[0m") 
                                 

def use_fragment():
    
    print(f"\nYou take the scroll fragment out of your bag, and gingerly unfurl it.") 
    print(scrollfrag * 5)
    _ = 'y'
    while _ != '':
        _ = input(f":::")

    print("It has a curious, almost familiar must.")
    print("For a moment, the suggestion of memory tickles your mind.")
    print(f"It departs as suddenly as it arrived. And you begin to read.")
    _ = 'y'
    while _ != '':
        _ = input(f":::")

    print(f"\n ... Perhaps the most defining advance of that long passed period was the discovery that the then foundational assumption, ")
    print("ancient and venerable in its origins, that there could be no true contradictions, could be fruitfully abandoned.")
    print("The seeds of this insight grew in reconsidering several domains, including abstract domains such as the mathematics of set theory,")
    print(" the formal theory of truth, and the incompleteness theorems, as well as concrete domains such as the legal system and the politics of identity. ")
    _ = 'y'
    while _ != '':
        _ = input(f":::")

    print(f"\nTake set theory, for instance. It was well known at the time, that using the then rules of the universe,")
    print("a contradiction could be derived from the assumption that for every predicate in the language of set theory, ")
    print("there is a set of exactly those things which satisfy the predicate, i.e., of exactly those things which have the property the predicate expresses. ")
    _ = 'y'
    while _ != '':
        _ = input(f":::")

    print(f"\nThis, rightly, was taken to be a great shame. It amounted to a mutilation of the seemingly crystal clear simple notion of a set -- of a collection. ")
    print("But, it was discovered by young rebellious group of theorists that we could preserve the naieve, ")
    print("beutiful view of sets, without collapsing into trivial mush! All we had to do, was weaken the rules in a precise, careful manner.")
    print("Similar results were found to apply in many other domains ...")

    _ = 'y'
    while _ != '':
        _ = input(f":::")

    print(f"\nThe fragment cuts off at this point.") 
    print("You carefully reroll it, and place it back in your bag.")
    print(f"Back to the action!\n")    


def pick_up(loot):
    x = ''
    
    for i in inventory:
        if i['item']['name'] == loot['name']:
            i['number'] += 1
            x = 'yes'
            
    if x != 'yes':
        inventory.append({'item': loot, 'number': 1})
        
    print(f"\n\033[3m***{Name} picked up a {loot['name']}.***\033[0m")    
    print(loot['icon'])
    print(f"\033[3m***{Name} put the {loot['name']} in their bag!***\033[0m")            

                                 

Potion = {"name": "potion", "description": "Increases health by 5.", "function": use_potion, "icon": potion}       
Fragment = {"name": "fragment", "description": "This is a fragment of a hoary scroll. It appears to be about paradoxes.", "function": use_fragment, "icon": scrollfrag} 


inventory = [{"item": Fragment, "number": 1}]



def scroll():

    _ = 'x'
    while _ != '' and _ != 'stats' and _ != 'attacks' and _ != 'items' and _ != 'use potion' and _ != 'use fragment':
        _ = input("__")

    while _ != '':

        if _ == 'stats':
            print(f"\nYou are {Name}, a skilled and dishevelled level {stats['level']} {Class}. ")
            print(f"Your health is currently {stats['health']}. ")
            print(f"Your physical strength is {stats['physical_strength']}. ")
            print(f"Your magical strength is {stats['magical_strength']}. ")
            print(f"Your speed is {stats['speed']}. ")
            _ = input(f"__")     



        elif _ == 'attacks':
            print(f"\nYour your repetoire of attacks currently contains '{attacks[0]['name']}' and '{attacks[1]['name']}'. ")
            print(f"{attacks[0]['name']} is a {attacks[0]['kind']} attack. It does a base damage of {attacks[0]['damage']}. ") 
            print(f"{attacks[1]['name']} is a {attacks[1]['kind']} attack. It does a base damage of {attacks[1]['damage']}. ")
            _ = input(f"__")       


        elif _ == 'items':
            if inventory != []:
                for i in inventory:
                    print(f"\n{i['item']['name']} :: {i['item']['description']} :: {i['number']} :: {i['item']['icon']}.")
                _ = input(f"__") 
            else:
                print(f"\nYour inventory is empty!")    
                _ = input(f"__")

        elif _ ==  'use potion':
            x = ''
            for i in inventory:
                if i["item"]["name"] == 'potion':
                    x = 'yes'

            if inventory == []:
                print(f"\nYou don't have any potions!")    
                _ = input(f"__")

            elif x == 'yes':
                use_potion(stats)    
                _ = input(f"__")       
                     
            else:
                print(f"\nYou don't have any potions!")    
                _ = input(f"__")
           
        elif _ == 'use fragment':
            x = ''
            for i in inventory:
                if i["item"]["name"] == 'fragment':
                    x = 'yes'

            if inventory == []:
                print(f"\nYou don't have any fragments!")    
                _ = input(f"__")

            elif x == 'yes':
                use_fragment()    
                _ = input(f"__")       
                     
            else:
                print(f"\nYou don't have any fragments!")    
                _ = input(f"__")





def Arctic_Wind(mage, demon):
    x = 2 * (mage['magical_strength']/demon["magical_strength"])
    y = demon['health'] - x
    demon['health'] = y
    print(mageicon, " -->", tornado * 5," -->",frowning_demon)
    return demon       

def Hex(mage, demon):
    x = mage['magical_strength']/demon["magical_strength"]
    y = demon['health'] - x
    demon['health'] = y
    print(mageicon," -->",lightning * 5," -->",frowning_demon)
    return demon   

def Fists_Of_Fire(warrior, demon):
    x = 2 * (warrior['physical_strength']/demon["physical_strength"])
    y = demon['health'] - x
    demon['health'] = y
    print(warrioricon," -->",fire, uppercut, fire, uppercut," -->",frowning_demon)
    return demon

def Uppercut(warrior, demon):
    x = warrior['physical_strength']/demon["physical_strength"]
    y = demon['health'] - x
    demon['health'] = y
    print(warrioricon," -->",uppercut * 5," -->",frowning_demon)
    return demon


def Smash(character, demon):
    x = 3 * (demon['physical_strength']/character["physical_strength"])
    y = character['health'] - x
    character['health'] = y
    if Class == 'warrior':
        print(frowning_demon," -->",smash * 5," -->",warrioricon)
    else:
        print(frowning_demon," -->",smash * 5," -->",mageicon)   
    return character 

def Bolt(character, demon):
    x = 3 * (demon['magical_strength']/character["magical_strength"])
    y = character['health'] - x
    character['health'] = y
    if Class == 'warrior':
        print(frowning_demon," -->",bolt * 5," -->",warrioricon)
    else:
        print(frowning_demon," -->",bolt * 5," -->",mageicon)
    
    return character 

def Explosion(character, demon):
    character["health"] = 0
    print(bomb * 10)
    return character 


Paradox_stats = {}
Paradox_Demon = demon('demon', 30, 30, 30, 2, [{"name": "Explosion", "function": Explosion, "kind": "physical", "damage": 'all health'}, {"name": "Explosion", "function": Explosion, "kind": "physical", "damage": 'all health'}, {"name": "Explosion", "function": Explosion, "kind": "physical", "damage": 'all health'}, {"name": "Explosion", "function": Explosion, "kind": "physical", "damage": 'all health'}])
Paradox_stats['max_health'] = 30
Paradox_stats["health"] = 30 
Paradox_stats["physical_strength"] = 30 
Paradox_stats["magical_strength"] = 30
Paradox_stats["speed"] = 2 
Paradox_stats["attacks"] = [{"name": "Explosion", "function": Explosion, "kind": "physical", "damage": 'all health'}, {"name": "Explosion", "function": Explosion, "kind": "physical", "damage": 'all health'}, {"name": "Explosion", "function": Explosion, "kind": "physical", "damage": 'all health'}, {"name": "Explosion", "function": Explosion, "kind": "physical", "damage": 'all health'}]
  


def Fast_Battle(character, moves, demon):
    print("***********************************************************")
    while character["health"] > 0 and demon["health"]>0:
        attack = ''
        while attack != moves[0]["name"] and attack != moves[1]["name"] and attack != moves[2]["name"] and attack != moves[3]["name"]:
            attack = input(f"\nWhich attack will you use?\n")  
        _ = 'y'
        while _ != '':
            _ = input(f":::\n")       
        
        if attack == moves[0]["name"]:
            moves[0]["function"](character, demon)
        elif attack == character["attacks"][1]["name"]:
            moves[1]["function"](character, demon)    
        elif attack == character["attacks"][2]["name"]:
            moves[2]["function"](character, demon)    
        elif attack == character["attacks"][3]["name"]:
            moves[3]["function"](character, demon)  

        print(f"\n{Name} used {attack}! ")
        _ = 'y'
        while _ != '':
            _ = input(f":::")

        if demon["health"] == 0 or demon["health"]<0:
            
            print(f"\n",frowning_demon * 2, skull * 2)
            print(f"\nRejoice! The foul demon is slain. ")
            print("*************************************************************")
            break
        elif demon["health"] < (demon["max_health"]/2) or demon["health"] == demon["max_health"]/2:
            print(f"\n",frowning_demon,blooddrop * 3)
            print(f"\nThe demon is seriously wounded ... And still going. ")
            _ = 'y'
            while _ != '':
                _ = input(f":::\n")
        elif demon["health"] < demon["max_health"] and demon["health"] > (demon["max_health"]/2):    
            print(f"\n",smiling_demon,blooddrop)
            print(f"\nAh ... That doesn't seem to have slowed it down all that much. ")
            _ = 'y'
            while _ != '':
                _ = input(f":::\n")

        z = random.randint(0,1)
        
        
        demon['attacks'][z]['function'](character, demon)
        print(f"\nThe Demon used {demon['attacks'][z]['name']}! ")
        _ = 'y'
        while _ != '':
            _ = input(f":::")

        if character["health"] == 0 or character["health"]<0:
            if Class == 'warrior':
                print(f"\n",warrioricon, skull * 3)
            else:
                print(f"\n",mageicon, skull * 3)    
            print(f"\nAlas fair, {Name}. Ye hardly knew ye! ")
            print(f"\nGAME OVER\n ")
            print("******************************************************************")
            break
        elif character["health"] < (character["max_health"]/2) or character == character["max_health"]/2:
            if Class == 'warrior':
                print(f"\n",warrioricon, blooddrop * 3)
            else:
                print(f"\n",mageicon, blooddrop * 3)
            
            print(f"\nTis but a flesh wound! ")
            attack = ''
            _ = 'y'
            while _ != '':
                _ = input(f":::")
        elif character["health"] < character["max_health"] and (character["health"]) > (character["max_health"]/2):    
            if Class == 'warrior':
                print(f"\n",warrioricon, blooddrop)
            else:
                print(f"\n",mageicon, blooddrop)
            
            print(f"\nThankfully, tis but a scratch. ")
            attack = ''
            _ = 'y'
            while _ != '':
                _ = input(f":::")


def Slow_Battle(character, moves, demon):
    while character["health"] > 0 and demon["health"]>0:
        z = random.randint(0,1)
        print("")

        demon['attacks'][z]['function'](character, demon)

        scroll()

        print(f"\nThe Demon used {demon['attacks'][z]['name']}! ")
        scroll()

        if character["health"] == 0 or character["health"]<0:
            if Class == 'warrior':
                print("")
                print(warrioricon, skull * 3)
            else:
                print("")
                print(mageicon, skull * 3)
            scroll()    
            print(f"\nAlas fair, {Name}. Ye hardly knew ye! ")
            print(f"\nGAME OVER\n ")
            print("******************************************************************")
            break
        elif character["health"] < (character["max_health"]/2) or character == character["max_health"]/2:
            if Class == 'warrior':
                print("")
                print(warrioricon, blooddrop * 3)
            else:
                print("")
                print(mageicon, blooddrop * 3)
            scroll()
            print(f"\nTis but a flesh wound! ")
            scroll()
        elif character["health"] < character["max_health"] and (character["health"]) > (character["max_health"]/2):    
            if Class == 'warrior':
                print("")
                print(warrioricon, blooddrop)
            else:
                print("")
                print(mageicon, blooddrop)
            scroll()
            print(f"\nThankfully, tis but a scratch. ")
            scroll()
        
        
        attack = ''
        while attack != moves[0]["name"] and attack != moves[1]["name"] and attack != moves[2]["name"] and attack != moves[3]["name"]:
            attack = input(f"\nWhich attack will you use?\n")     
        
        print("")
        if attack == moves[0]["name"]:
            moves[0]["function"](character, demon)
        elif attack == moves[1]["name"]:
            moves[1]["function"](character, demon)    
        elif attack == moves[2]["name"]:
            moves[2]["function"](character, demon)    
        elif attack == moves[3]["name"]:
            moves[3]["function"](character, demon)  

        scroll()    

        print(f"\n{Name} used {attack}! ")
        scroll()

        if demon["health"] == 0 or demon["health"]<0:

            print("")
            print(frowning_demon * 2, skull * 2)
            scroll()

            print(f"\nRejoice! The foul demon is slain. ")
        
            print("*****************************************************************")
            break
        elif demon["health"] < (demon["max_health"]/2) or demon["health"] == demon["max_health"]/2:
            
            print("")
            print(frowning_demon,blooddrop * 3)
            scroll()
            print(f"\nThe demon is seriously wounded ... And still going. ")
            scroll()
        elif demon["health"] < demon["max_health"] and demon["health"] > (demon["max_health"]/2):  
            print("")
            print(smiling_demon,blooddrop)  
            scroll()
            print(f"\nAh ... That doesn't seem to have slowed it down all that much. ")
            scroll()

        
print(f"\nWelcome to level 1.")
print(f"Our story begins in Plumwood Forrest ... \n")

for i in range(5):
    print(tree_one * 15)
_ = 'y'
while _ != '':
    _ = input(f"\n::: (\033[3m***Press enter to scroll the screen, when you see the ':::' icon.***\033[0m)")    

print(f"\n\033[3m'What in the world ..........'\033[0m")
print(f"\033[3m'Hey! Hey you! Wake up! Wake up!'\n\033[0m")

print("Yours eyes slowly open. There is a sharp, painful ringing in your ears.")
print("The grey morning glare strains your gravelled eyes. ")
_ = 'y'
while _ != '':
    _ = input(f":::")

print(f"\n\033[3m'What are you doing sleeping at the side of the road?'\033[0m")
print(f"\033[3m'Why so dishevelled?'\033[0m")
print(f"\033[3m'I gather you're not from around these parts?'\033[0m")
_ = 'y'
while _ != '':
    _ = input(f":::")


print(f"\nYou feel a few tears form. The gravel dissolves enough for your eyes come into focus, reluctantly.")
print("You see the stooped, wizened man hovering over you, asking disconcertingly disconcerting questions.")
_ = 'y'
while _ != '':
    _ = input(f":::")

print(f"\nWhat are you doing? How did you get here? What happened?")
print("You can't seem to catch any of your thoughts.")
print("As gossamer threads in a strong wind, they remain resolutely incohate.")
print("You notice the old man's left eyebrow is bobbing with increasing alacrity.")
print("He is perturbed by the silence.")
_ = 'y'
while _ != '':
    _ = input(f":::")

print(f"\n\033[3m'Emm ... Tell me, my dishevelled friend, what is your name?'\033[0m")

print(f"\nAh gods, what is your name? Can't remember, can you? ")
print("Better say something!")

Name = input(f"\n\033[3m'Well ... What is your name?'\033[0m\n")

print(f"\n\033[3m'Ah, they speak!!.\033[0m ")


answer = input(f"\033[3m'Alas, you must forgive an old man his aged ears. Your name is {Name}, yes?'\033[0m\n")
if answer != 'yes' and answer != 'no':
    print(f"\n\033[3m(***Please answer 'yes' or 'no'.***)\033[0m")
    _ = 'y'
    while _ != '':
        _ = input(f":::")

    answer = ''
    while answer != 'yes' and answer != 'no':
        answer = input(f"\n\033[3m'So, your name is {Name}, yes?'\033[0m\n")



    
if answer == 'no':
    Name = input(f"\n\033[3m'Damn these aged ears! Then what is your name?'\033[0m\n")

if Name == 'Samakin':
    print(f"\nSammy!", heart * 8, "I love you buddy! You are my all time favorite person, and a very righteous dude!")
    print("I hope you like my game! ")
    _ = 'y'
    while _ != '':
        _ = input(f":::")

print(f"\n\033[3m'Welcome to Paragon, {Name}.'\033[0m ")
print("\033[3m'Though by the looks of you, you will likely not find it very welcoming.'\033[0m ")
print(f"\033[3m'Ah, the way we used to be! '\033[0m ") 
print(f"\033[3m'You would have loved it.'\033[0m ")
_ = 'y'
while _ != '':
    _ = input(":::")

print(f"\nWait. What does he mean by that? What does he see?")
print("Worried, you realize you haven't processed the last few things the old man has said. ")
print("Concentrate! This could be important. ")
_ = 'y'
while _ != '':
    _ = input(":::")

print(f"\n\033[3m'The land and we were beautiful, tolerant, diverse.'\033[0m ")
print(f"\033[3m'Anywhere flowers bloomed, they did so with dazzling variety. Thousands of kinds if any at all.'\033[0m ")
print(f"\033[3m'In the academies, in the halls of the palace, in this very forest ... '\033[0m ")
print(f"\033[3m'So many things were different before the Collapse.'\033[0m ")
_ = 'y'
while _ != '':
    _ = input(":::")

print(f"\nThe old man takes his time over the word 'Collapse'. As though he is sampling it. ")
print("He takes a bite, chews it, tastes it. He pauses for a moment, turns his head to the side, and spits with venom. ")
print("It is distasteful. Vile, even. ")
print("Curious.")
_ = 'y'
while _ != '':
    _ = input(":::")

print(f"\n\033[3m'Ach, I'm rambling. Of course you know all of this.'\033[0m")
print("\033[3m'But still, you seem ... disoriented. And frankly, disorienting.'\033[0m") 
print(f"\033[3m'There's something about you, {Name}. Something ... untidy ... transgressive ... wild.'\033[0m ")
print("\033[3m'Just look how I found you, propped up by the trunk of an old, hollowed Plumwood.'\033[0m ")

answer = ''
while answer != 'yes' and answer != 'no':
    answer = input(f"\033[3m'Perhaps you would like to know about the Collapse?'\033[0m\n")

if answer == 'yes':
    print(f"\nYou notice a hint of a wry smile on the man's face. ")
    print("That meant something to him. ")
    print("But what? ")
    _ = 'y'
    while _ != '':
        _ = input(":::")

    print(f"\n\033[3m'A wise choice. Fortune favors the knowledgable.'\033[0m ")
    print("\033[3m'Where to begin? ... '\033[0m ")
    print(f"\033[3m'Let's see. Paragon, like many worlds, is governed by a very general set of laws.'\033[0m ")
    print(f"\033[3m'Structural rules that everything must obey.'\033[0m ")
    print(f"\033[3m'Unlike other worlds though, in Paragon these laws are chosen.'\033[0m ")
    print(f"\033[3m'This choice, rather than the world itself, dictates the rules the world and everything in it follows.'\033[0m ")
    print(f"\033[3m'As such, these laws can change ... if the high priests are mad enough to so choose.'\033[0m ")
    _ = 'y'
    while _ != '':
        _ = input(":::")

    print(f"\nHe pauses and a pained look takes shape on his weathered face. ")
    print("It seems to you that his face is very used to wearing this look. ")
    print("You want to say something to comfort him. But you can think of nothing. ")
    _ = 'y'
    while _ != '':
        _ = input(f":::")

    print(f"\n\033[3m'Before, the laws were permissive, tolerant, pluralistic.'\033[0m ")
    print(f"\033[3m'But at the time of the last choosing, the high priests changed all of that.'\033[0m ")
    print("\033[3m'What could possibly have possessed them?'\033[0m ")
    print("\033[3m'No one knows ... '\033[0m ")
    _ = 'y'
    while _ != '':
        _ = input(f":::")
 
    print(f"\nHe trails off for a moment.")
    print("Some hidden thought haunts his eyes.")
    print("After a moment, and a few measured blinks, his cold marble blue eyes refocus. ")
    _ = 'y'
    while _ != '':
        _ = input(f":::")

    print(f"\n\033[3m'We do know the change was brutally enforced.'\033[0m ")
    print("\033[3m'Every being that ... opposed the change ... was swifly broken and brought to heel.'\033[0m ")
    print("\033[3m'Paragon is now a very different place.'\033[0m ") 
    print(f"\033[3m'Powerful, efficient, rigid, subject to a suffocating malaise.'\033[0m ")
    _ = 'y'
    while _ != '':
        _ = input(f":::")

elif answer == 'no':
    print(f"\n\033[3m'Yes well, of course you already know about the Collapse. How could you not?'\033[0m ")
    _ = 'y'
    while _ != '':
        _ = input(f":::")  


print(f"\n\033[3m'I wonder though, does your sudden appearance signal something portentious?'\033[0m ")
print(f"\033[3m'Are you, perchance, a mighty warrior, or a venerable mage ...'\033[0m")
_ = 'y'
while _ != '':
    _ = input(f":::")
  

print(f"\nYou feel a faint tingle of recognition run through you. ")
print("You look down at your hands. ")
print("Yes, you think. That is the first thing that sounds right.")
_ = 'y'
while _ != '':
    _ = input(":::")

Class = ''
while Class != 'warrior' and Class != 'mage':
    Class = input(f"\n\033[3m'Well ... are you a warrior or a mage?'\033[0m\n")


demon_stats = {}
enemy = demon('demon', 6, 8, 8, 15, [{"name": "Smash", "function": Smash, "kind": "physical", "damage": 3}, {"name": "Bolt", "function": Bolt, "kind": "physical", "damage": 3}, {"name": "'Not Available'", "function": Smash, "kind": "physical", "damage": 2}, {"name": "'Not Available'", "function": Smash, "kind": "physical", "damage": 2}])
demon_stats['max_health'] = 6
demon_stats["health"] = 6 
demon_stats["physical_strength"] = 8 
demon_stats["magical_strength"] = 8
demon_stats["speed"] = 15 
demon_stats["attacks"] = [{"name": "Smash", "function": Smash, "kind": "physical", "damage": 3}, {"name": "Bolt", "function": Bolt, "kind": "physical", "damage": 3}, {"name": "'Not Available'", "function": Smash, "kind": "physical", "damage": 2}, {"name": "'Not Available'", "function": Smash, "kind": "physical", "damage": 2}]
  

stats = {}
attacks = []

if Class == "warrior":
    character =  warrior(f"{Name}", 10, 12, 4, 6, [{"name": "Uppercut", "function": Uppercut, "kind": "physical", "damage": 1}, {"name": "'Fists Of Fire'", "function": Fists_Of_Fire, "kind": "physical", "damage": 2},  {"name": "'Not Available'", "function": Smash, "kind": "physical", "damage": 2}, {"name": "'Not Available'", "function": Smash, "kind": "physical", "damage": 2}])
    stats["name"] = Name 
    stats["class"] = Class
    stats["max_health"] = 10
    stats["health"] = 10 
    stats["physical_strength"] = 12 
    stats["magical_strength"] = 4 
    stats["speed"] = 6
    stats["level"] = 5
    stats["exp"] = 0
    attacks.append({"name": "Uppercut", "function": Uppercut, "kind": "physical", "damage": 1})
    attacks.append({"name": "Fists Of Fire", "function": Fists_Of_Fire, "kind": "physical", "damage": 2})
    attacks.append({"name": "'Not Available'", "function": Smash, "kind": "physical", "damage": 2})
    attacks.append({"name": "'Not Available'", "function": Smash, "kind": "physical", "damage": 2})
    print(f"\n***", warrioricon * 5, "***")
elif Class == "mage": 
    character =  mage(f"{Name}", 10, 4, 12, 6, [{"name": "Hex", "function": Hex, "kind": "magical", "damage": 1}, {"name": "Arctic Wind", "function": Arctic_Wind, "kind": "magical", "damage": 2}, {"name": "'Not Available'", "function": Smash, "kind": "physical", "damage": 2}, {"name": "'Not Available'", "function": Smash, "kind": "physical", "damage": 2}])
    stats["name"] = Name 
    stats["class"] = Class
    stats["max_health"] = 10
    stats["health"] = 10
    stats["physical_strength"] = 4 
    stats["magical_strength"] = 12 
    stats["speed"] = 6
    stats["level"] = 5
    stats["exp"] = 0
    attacks.append({"name": "Hex", "function": Hex, "kind": "magical", "damage": 1})   
    attacks.append({"name": "Arctic Wind", "function": Arctic_Wind, "kind": "magical", "damage": 2})
    attacks.append({"name": "'Not Available'", "function": Smash, "kind": "physical", "damage": 2})
    attacks.append({"name": "'Not Available'", "function": Smash, "kind": "physical", "damage": 2})
    print(f"\n***", mageicon * 5, "***")


print(f"\n\033[3m'I see. What a strange and interesting day this is, running into a {Class}.'\033[0m ")
print(f"\033[3mAnd strewn unconscious on the forest floor at that!\033[0m ")
print(f"\033[3m'What happened, {Name}? How ....\033[0m") 
_ = 'y'
while _ != '':
    _ = input(":::") 

print(f"\nA furious, bone-chilling growl drowns out the old man's voice.")
print(f"A menacing snarl follows, and then, more menacing still, silence.")
_ = 'y'
while _ != '':
    _ = input(":::")

print(f"\n\033[3m'DID YOU HEAR THAT?'\033[0m ")
_ = 'y'
while _ != '':
    _ = input(":::")


print(f"\nYou absolutely heard that!! What the fuck was that??")
print("You whip your head around to face the old man.")
print("A bead of sweat has formed on his brow.")
print("He is clearly fearful.")
print("And yet you notice a hint of something else on his face too ... satisfaction???")
_ = 'y'
while _ != '':
    _ = input(":::")
 
print(f"\n\033[3m'It's an enforcer demon, {Name}!!'\033[0m ")
print(f"\033[3m'It must have sensed you!!'\033[0m ")
print(f"\033[3m'We need to get out of here.'\033[0m ")
print(f"\033[3m'NOW!!!'\033[0m ")
_ = 'y'
while _ != '':
    _ = input(":::")

print(f"\nAs the demonic snarls resound, the old man turns, and sprints off with unexpected speed.")
print("For a moment you are surpirsed, and everything is still.")
print(f"And then you see it, nightmarish, slouching towards you, hissing, spitting, growling.")
_ = 'y'
while _ != '':
    _ = input(":::")  

print("")
print(frowning_demon * 5)
_ = 'y'
while _ != '':
    _ = input(":::")  



print(f"\n\033[3m***Tutorial Sidebar:\033[0m ")
Tutorial = ''
while Tutorial != 'yes' and Tutorial != 'no':
    Tutorial = input(f"\033[3mWould you like to see a tutorial about battles?***\033[0m\n")
if Tutorial == 'yes':

    print(f"\n\033[3m***Whenever an enemy approaches, you will be able to choose an action. Either you can run, or fight.\033[0m ")
    print("\033[3mWhen asked: 'What will you do?', repsond either: 'run' or 'fight'.\033[0m ")
    print("\033[3mIf you choose to run, a calculation based upon your speed and the enemy's speed will determine whether you succeed.***\033[0m ") 
    _ = 'y'
    while _ != '':
        _ = input(":::")

    print(f"\n\033[3m***If you choose to fight, or if you fail to run, you will be asked which attack to use.\033[0m ")
    print("\033[3mWhen asked: 'Which attack will you use?', respond with the name of one of your attacks.\033[0m ")
    print("\033[3mIf you are faster, you will attack first. Otherwise, the enemy will attack first. The battle will the proceed in a turn based manner.\033[0m ")
    print(f"\033[3mDamage is detemrined by your strength, the enemy's strength, and the base damage of the attack.***\033[0m ")
    _ = 'y'
    while _ != '':
        _ = input(":::")


    stats_check =''
    while stats_check != 'yes' and Tutorial != 'no':   
        stats_check = input(f"\033[3m\n***Would you like to check your stats?***\033[0m\n")

    if stats_check == 'yes':
        print(f"\n\033[3m***You are {Name}, a skilled and dishevelled level {stats['level']} {Class}.\033[0m ")
        print(f"\033[3mYour health is currently {stats['health']}.\033[0m ")
        print(f"\033[3mYour physical strength is {stats['physical_strength']}.\033[0m ")
        print(f"\033[3mYour magical strength is {stats['magical_strength']}.\033[0m ")
        print(f"\033[3mYour speed is {stats['speed']}.***\033[0m ")
        _ = 'y'
        while _ != '':
            _ = input(":::")
 
        print(f"\n\033[3m***In future, if you would like to check your stats, whenever the '__' icon appears, instead of ':::',\033[0m ")
        print(f"\033[3mas well as clicking enter to just scroll, you can type in 'stats', and your stats will appear.***\033[0m ")
        
    else: 
        print(f"\n\033[3m***Fortune sometimes favors the ill-prepared!***\033[0m ")     


    attacks_check = ''
    _ = 'y'
    while _ != '':
        _ = input(":::")
    while attacks_check != 'yes' and attacks_check != 'no':
        attacks_check = input(f"\n\033[3m***Would you like to see your current repetoire of attacks?\033[0m\n") 

    if attacks_check == 'yes':
        print(f"\n\033[3m***Your your repetoire of attacks currently contains '{attacks[0]['name']}' and '{attacks[1]['name']}'.\033[0m ")
        print(f"\033[3m{attacks[0]['name']} is a {attacks[0]['kind']} attack. It does a base damage of {attacks[0]['damage']}.\033[0m ") 
        print(f"\033[3m{attacks[1]['name']} is a {attacks[1]['kind']} attack. It does a base damage of {attacks[1]['damage']}.***\033[0m ")
        _ = input(":::")
 
        print(f"\n\033[3m***In future, if you would like to see your attacks, whenever the '__' icon appears, you can type in 'attacks', and your attacks will appear.\033[0m")
        print(f"\033[3mBack to the action!***\033[0m")
        scroll()

    else:
        print(f"\n\033[3m***A curious choice.\033[0m ")
        print(f"\033[3mBack to the action!***\033[0m") 
         

else:
    print(f"\n\033[3m***Hmm. A curious choice, {Name}. Back to the action.***\033[0m ")     
    


action_check = ''
while action_check != 'run' and action_check != 'fight':
    action_check = input(f"\n\033[3m***The demon approaches. What will you do?\033[0m***\n")


if action_check == 'run': 
    if stats['speed'] > demon_stats["speed"]:
        print(f"\nYou take one look at the demon, and take off after the old man as fast as you can!. ")
        print("You can hear the demon lumbering after you. Blessedly, that terrifying noise gets quieter and quieter. ")
        _ = input("__")
        print(f"\nYou are swift, and have escaped the demon! ")
        _ = input("__")  

     
    else:
        print(f"\nYou take one look at the demon, and take off after the old man as fast as you can!. ")
        print("You can hear the demon lumbering after you. Nauseatingly, the terrifying noise gets louder and louder. ")
        scroll()
        print(f"\nAlas! The demon is too fast. It is right on your heels. You must fight!! ")
        scroll()  

        

        print(f"\nA potent, almost virulent, mixture of fear and excitement?? runs through you.")
        print("You take a deep breath, and steady yourself. ")    
        print("Let's do this!")
        _ = 'y'
        while _ != '':
            _ = input(":::")

        answer = ''
        while answer != 'yes':
            answer = input(f"\n\033[3m***Are you ready???***\033[0m\n")    
        
        print (f"\n***LET THE BATTLE COMMENCE!***")
        scroll()  
        Slow_Battle(stats, attacks, demon_stats)

        if stats["health"] > 0:
            scroll()
            print(f"\nThe demon takes an age to fall. ")
            print("When its bloated body is finally still on the forrest floor, you take a chasmically deep breath.")
            print("You did it. You are somehow still alive!!!")

            scroll()
        
            print(f"\n\033[3m***Stats Sidebar:\033[0m ")
    
            print("\033[3mYou have gained 5 experience points.\033[0m")
            stats["exp"] += 5  
            stats["level"] += 1
            stats["max_health"] += 1
            stats["magical_strength"] += 1
            stats["physical_strength"] += 1
            stats["speed"] += 1
            print(f"\033[3mYou have grown one level. You are now level {stats['level']}.\033[0m ")
            print("\033[3mYour stats have increased.\033[0m")
            print ("\033[3mBack to the action!***\033[0m")
            scroll() 
                

             
            print(f"\nYou collapse to the ground, as the river of adrenaline coursing through your veins begins to ebb.") 
            print("What the hell was that thing?")  
            print("And how did you fight so well? ")
            scroll()

            print(f"\nYour thoughts begin sprialling out of your grip. ")
            print("And just then you notice the old man gingergly poke his head out from behind a gnarled oak tree. ")
            print("His expression is hard to understand. ")
            print("You think perhaps it is a mix of sheer surprise and a giddy glee. ")
            _ = 'y'
            while _ != '':
                _ = input(":::")

            print(f"\n\033[3m'{Name}!!! That was incredible!!!'\033[0m ") 
            print(f"\033[3m'I thought when it caught up to you, you were dead.'\033[0m ")
            print(f"\033[3m'But no!!! Amazing.'\033[0m ")
            print(f"\033[3m'Perhaps I am right about you afterall, {Name}.'\033[0m ")
            _ = 'y'
            while _ != '':
                _ = input(":::")

            print(f"\nEven amidst the bone-deep tiredness you feel a flash of anger, at this further vague, knowing suggestion.")
            print("You will need to find out what the old man knows.")
            print("Or what he thinks he knows!")    
            _ = 'y'
            while _ != '':
                _ = input(":::")

            print(f"\n\033[3m'Ah look. It seems there is an item poking out of the demon's pouch.'\033[0m ")
            print(f"\033[3m'Terrifying though they are, they do often have some very useful trinkets.'\033[0m ")
            print(f"\033[3m'Why don't you go see what it is?'\033[0m ")
            _ = 'y'
            while _ != '':
                _ = input(":::")

            print(f"\nYour internal ire momentarily interrupted, you slowly walk over to the demon's corpse." )
            print("There is indeed a vial of shiny, purple liquid poking out of the demon's pouch.")
            print("You very hesitantly reach in and remove the vial.") 
            _ = 'y'
            while _ != '':
                _ = input(":::")

            pick_up(Potion)

            _ = 'y'
            while _ != '':
                _ = input(":::")

            print(f"\nAs you place the potion in your backpack, you notice a scroll 'fragment' already in there. ")
            print(f"As with distressingly many things, you have no memory of this.")
            print(f"Perhaps there is some key to your past in there? Some clue?")
            print(f"You should ivestigate this later, you think.")
            _ = 'y'
            while _ != '':
                _ = input(":::")
        
            print(f"\n\033[3m***Item Tutprial:\033[0m")
            check = ''
            while check != 'yes' and check != 'no':
                check = input("\033[3mWould you like to check your inventory?***\033[0m\n")
            if check == "yes":    
                for i in inventory:
                    print(f"\n\033[3m***{i['item']['name']} :: {i['item']['description']} :: {i['number']}.***\033[0m")
                _ = 'y'
                while _ != '':
                    _ = input(":::")    

                print(f"\n\033[3m***The first slot is the name of the item.\033[0m ")
                print("\033[3mThe second is a description of the item.\033[0m ")
                print("\033[3mAnd the third is how many of the item you have.***\033[0m ")
                _ = 'y'
                while _ != '':
                    _ = input(":::")

                print(f"\n\033[3m***In future, if you would like to check your inventory, type 'items' when the '__' icon appears.\033[0m ")
                print(f"\033[3mIn future, if you would like to use an item from your inventory, type 'use' and the name of the item when the '__' icon appears.\033[0m ")
                print("\033[3mSo to use your potion, for instance, type in 'use potion' when the '__' icon appears.\033[0m ")
                print(f"\033[3mBack to the action!***\033[0m")
            
            else:
                print(f"\n\033[3m***An odd choice, {Name}.\033[0m")
                print(f"\033[3mBack to the action!***\033[0m")

            
            scroll()

            print(f"\nWithout any warning, the demon's body decays at an unnatural pace.")
            print("Its flesh dessicates, and its skeleton collapses.")
            print("One moment it is there.")
            print("And the next it is gone, in a puff of miasmic dust.")
            scroll()

            print(f"\nYou leap backwards, troubled!")
            print("For some reason this bothers you more than anything that has yet happened.")
            print("Things shouldn't be that sharp, you think.")
            print("Deeply troubled, you walk back over to the old man, who has keenly observed this puzzling interaction.")
            print("He belessedly silent on this point.")
            scroll()

            print(f"\n\033[3m'Always good to make use of what we find, eh?.'\033[0m ")
            print("\033[3m'I venture that potion would do you well!'\033[0m")
            print("\033[3m'Now, we need to get you out of the forrest.' \033[0m ")
            print("\033[3m'If that demon sensed you so quickly, there are likely several others nearby.'\033[0m ")
            print("\033[3m'And they may not be as cuddly as that one!'\033[0m ")
            scroll()

            print(f"\nAs soon as the disasterously prescient warning leaves the old man's lips, a demented cackle reverberates around the glade. ")
            print("A look base terror crowds his face.")
            print("You have a feeling that the cackler, whatever it is, is something you would rather avoid.")
            _ = 'y'
            while _ != '':
                _ = input(":::")


            print(f"\nThe old man's lips struggle to come unstuck. ")
            print("Before, he was fearful. Now, he is terrified.")
            print("Prising his lips apart, a Herculian effort, he finally manages to give words to his fear. ")
            _ = 'y'
            while _ != '':
                _ = input(":::")

            print(f"\n\033[3m'That is a Paradox Hunter.'\033[0m ")
            print("\033[3m'There is no time to explain.' \033[0m ")
            print("\033[3m'They are slow. But by the sounds of it, this one is closeby.'\033[0m ")
            print("\033[3m'If we run right now, we can escape it, and this forrest!'\033[0m ")
            print("\033[3m'Come with me, if you want to live!'\033[0m ")
            scroll()

            action_check = ''
            while action_check != 'run' and action_check != 'fight':
                action_check = input(f"\n\033[3m***The paradox hunter approaches. What will you do? Run, or fight?***\033[0m\n")
            
            if action_check == 'run':
                print(f"\nYou look at the expression on the old man's face, the pleading in his eyes.")
                print("And you nod, firmly.")
                print("He deeply breathes a sigh of relief.")
                _ = 'y'
                while _ != '':
                    _ = input(":::")

                print(f"\n\033[3mAway with us then!\033[0m ")
                print(f"\033[3mThere is no time to waste!\033[0m ")
                _ = 'y'
                while _ != '':
                    _ = input(":::")

                print(f"\nThe old man takes off at an almost manic pace.")
                print(f"And you are right there beside him!")


                _ = 'y'
                while _ != '':
                    _ = input(":::")
                
                print(f"\n\033[3m***Well done, {Name}!\033[0m ") 
                print(f"\033[3m***You have completed level 1.\033[0m ")   
                print("\033[3mWould you like to save the game?\033[0m ") 
                print("\033[3mFair warning: if you don't, you won't be able to play level 2!***\033[0m ")
                _ = 'y'
                while _ != '':
                    _ = input(":::")

                save = ''
                while save != 'yes' and save != 'no':
                    save = input(f"\n\033[3m***So, would you like to save the game?***\033[0m\n")

                if save == 'no':
                    print(f"\n\033[3m***I hope you enjoyed my level.***\033[0m ")

                else: 
                    print(f"\n\033[3m***You have saved the game! On to level 2!***\033[0m ")
                    with open("Completion.csv", "w") as completion_file:
                        completion_file.write("level 1,complete.") 
                    with open("Stats.csv", "w") as stats_file:
                        for i in stats:
                            stats_file.write(f"{i},{stats[i]}\n")
                    with open("Inventory.csv", "w") as inventory_file:
                        for i in inventory:
                            inventory_file.write(f"{i['item']['name']},{i['number']}\n")   
                    with open("Attacks.csv", "w") as attacks_file:
                        for i in attacks:
                            attacks_file.write(f"name,{i['name']}\n")            
                                   

            else: 
                print(f"\nYou look again at the expression on the old man's face, and the pleading in his eyes.")
                print("But from somewhere deep within you, resolve surges, oceanic in immensity.")
                print("You slowly shake your head. ")
                _ = 'y'
                while _ != '':
                    _ = input(":::")

                print(f"\nThe old man slumps.")
                print(f"As though he has just lost the last remnants of something essential.")
                _ = 'y'
                while _ != '':
                    _ = input(":::")

                print(f"\n\033[3m'Then we will die together.'\033[0m ")
                print(f"\033[3m'There is nothing left for me ...' \033[0m ")
                scroll()

                print(f"\nThe old man takes off his cloak.")
                print(f"And slowly turns to face the nightmare that has just entered the glade.")
                scroll()




                print(f"\nYou follow his gaze and lay your eyes on the Hunter.")
                print("Where the Enforcer had been bestial, gutteral, somatic, the Paradox Hunter is refined, understated, cerebral.")
                print("It strides into the glade, its movement languid, cocksure even. ")
                print("When its eyes come to rest on the old man, its aquiline face breaks into a full, toothy smile.")
                scroll()

                print(f"\n\033[3m'Vale ... What an unbridled pleasure it is to see you again.'\033[0m")
                print(f"\033[3m'It has been far too long.'\033[0m")
                scroll()

                print(f"\nFor a moment you wonder if the Hunter is speaking to you. Perhaps it knows you. Are you Vale?")
                print("But then you see its scarlet pupils are fixed firmly on the old man.")
                print("They simmer with recognition.")
                scroll()

                print(f"\n\033[3m'And which one are you again?'\033[0m")
                print(f"\033[3m'I never could tell you apart.'\033[0m")
                scroll()


                print(f"\nYou notice a momentary flicker of annoyance dance across the Hunter's face.")
                print("It flashes a razor sharp canine. ")
                print("And despite yourself, you feel your whole body wracked by an instinctual fear.")
                print("This, it transpires, is but a candle next to the bonfire that consumnes you when it suddenly turns and trains those scarlet pupils on you.")
                scroll()

                print(f"\n\033[3m'And who have we hear, Vale?'\033[0m")
                print(f"\033[3m'How have we not found them already?'\033[0m")
                print(f"\033[3m'They absolutley wreak of ... transgression.'\033[0m")
                scroll()

                print(f"\nYou have no idea what to say.")
                print("And even if you did, you are not sure you could manage a syllable, let alone a sentence.")
                scroll()


                print(f"\n\033[3m'Leave them alone, Russellian.'\033[0m")
                print(f"\033[3m'Whatever it is you want to settle, you can settle with me.'\033[0m")
                scroll()

                print(f"\nThe demon smiles even wider.")
                print("Gleeful at the tremor in Vale's voice.")
                scroll()

                print(f"\n\033[3m'Ah, you do you remember me, Vale.'\033[0m")
                print(f"\033[3m'How perfectly equisite.'\033[0m")
                print(f"\033[3m'Would that I could.'\033[0m")
                print(f"\033[3m'But you know just as well as I, that I can do no such thing.'\033[0m")
                print(f"\033[3m'This one will have to be tested.'\033[0m")
                print(f"\033[3m'There is nothing for it.'\033[0m")
                print(f"\033[3m'And if they fail ... Well, we'll none of us be long for this world.'\033[0m")
                scroll()

                print(f"\nRussellian turns to face you once again.")
                print("Cleary, it is revelling in its task. ")

                print(f"\n\033[3m'Now listen well. I am going to test you.'\033[0m")
                print(f"\033[3m'I am certain that you will fail.'\033[0m")
                print(f"\033[3m'But we must follow the rules, mustn't we?'\033[0m")
                print(f"\033[3m'I will ask you a series of three questions.'\033[0m")
                print(f"\033[3m'If you falter, you will face me in combat, and you will surely die.'\033[0m")
                scroll()

                print(f"\n\033[3m'The first two questions are yes/no.'\033[0m")
                print(f"\033[3m'Those are the only acceptable answers.'\033[0m")
                print(f"\033[3m'You had better choose wisely.'\033[0m")
                scroll()

                print(f"\n\033[3m'The third and final question, should you make it that far, is multiple choice.'\033[0m")
                print(f"\033[3m'There will be four options, named 1, 2, 3, and 4.'\033[0m")
                print(f"\033[3m'Give your answers to me as those numbers separated by commas and spaces.'\033[0m")
                print(f"\033[3m'So, for instance, if you think that 1 and 2 and 3 are correct answers, say '1, 2, 3'. '\033[0m")
                print(f"\033[3m'Good luck. You will need it.'\033[0m")
                scroll()



                ready_check = ''
                while ready_check != 'yes':
                    ready_check = input(f"\n\033[3m***Are you ready?***\033[0m\n")
                print(f"\nYou do not know what to expect.")
                print("What kind of questions does a demon ask?") 
                print("You take a moment to find your center.")
                print("You are about to find out!")  
                scroll()
                
                print(f"\nRussellian takes the sight of us in, and smiles wide.")
                print("Its whole body is taught, entranced in its role.")
                print("At least one you is confident!")
                scroll()

                print(f"\n\033[3m'Now listen well old man.'\033[0m")
                print(f"\033[3m'Any help from you, even the slightest hint, and we all immediately die.'\033[0m")
                print(f"\033[3m'The integrity of the test is paramount!'\033[0m")
                print(f"\033[3m'Understood?'\033[0m") 
                scroll()

                print(f"\nYou look over at Vale.")
                print("He gives one, sharp nod. ")
                print("And remains silent.")
                print("You are on your own.")
                scroll()

                print(f"\n\033[3m'Fabulous!'\033[0m")
                print(f"\033[3m'Then here we go.'\033[0m")
                print(f"\033[3m'I, Rusellian, shall ask you some simple questions about the mathemaatics of set theory.'\033[0m")
                print(f"\033[3m'As everyone knows, a set is a mathematical object. It is an extensional collection of things, '\033[0m")
                print(f"\033[3m'i.e., a collection of things whose identity is determined purely by the identity of its members.'\033[0m")
                question_1 = ''
                while question_1 != 'yes' and question_1 != 'no':
                    question_1 = input(f"\n\033[3mQuestion 1: 'Is there an empty set -- a set which has no members?'\033[0m\n")
                if question_1 == 'no':
                    print(f"\n\033[3m'I knew it!'\033[0m")
                    print(f"\033[3m'I could smell it on you.'\033[0m")
                    print(f"\033[3m'Your whole being wreaks of it!'\033[0m")
                    scroll()

                    print(f"\n\033[3m'Of course there is!'\033[0m")
                    print(f"\033[3m'If there were not, how would anything work?!'\033[0m")
             
                    scroll()

                    print(f"\n\033[3m'Now you die!'\033[0m")
                    scroll()

                    ready_check = ''
                    while ready_check != 'yes':
                        ready_check = input(f"\nThe Paradox Hunter is about to attack. Are you ready to face it?\n")
                    print(f"\nLet the battle commence!")

                    Fast_Battle(stats, attacks, Paradox_stats)
                    


                else:
                    print(f"\n\033[3m'Hmm. Very good.'\033[0m")
                    print(f"\033[3m'Of course there is.'\033[0m")
                    print(f"\033[3m'If there were not, unmitigated chaos would ensue!'\033[0m")
                    print(f"\033[3m'On to the next question.'\033[0m")
                    scroll()

                    question_2 = ''
                    while question_2 != 'yes' and question_2 != 'no':
                        question_2 = input(f"\n\033[3mQuestion 2: 'Is it the case that for every property, there is a set of exactly those things which have that property?'\033[0m\n")
                    if question_2 == 'yes':
                        print(f"\n\033[3m'I knew it!'\033[0m")
                        print(f"\033[3m'I could smell it on you.'\033[0m")
                        print(f"\033[3m'Your whole being wreaks of it!'\033[0m")
                        scroll()

                        print(f"\n\033[3m'Of course there is not|!'\033[0m")
                        print(f"\033[3m'If there were then, there would be a set of all sets that do not contain themselves.'\033[0m")
                        print(f"\033[3m'And this set contains itself just in case it does not contain itself.'\033[0m")
                        print(f"\033[3m'A blatant, disgusting contradiction.'\033[0m")
                        scroll()

                        print(f"\n\033[3m'Now you die!'\033[0m")
                        scroll()

                        ready_check = ''
                        while ready_check != 'yes':
                            ready_check = input(f"\nThe Paradox Hunter is about to attack. Are you ready to face it?\n")
                        print(f"\nLet the battle commence!")

                        Fast_Battle(stats, attacks, Paradox_stats)    
                   
                

             
    
                    else:
                        print(f"\n\033[3m'Again, very good. Of course it's not the case.'\033[0m")
                        print(f"\033[3m'It is a preposterous, pernicious, paradoxical proposition!'\033[0m")  
                        print(f"\033[3m'A crutch for the naieve of mind and heart.'\033[0m")
                        scroll()
                        
                        print(f"\n\033[3m'But do you know why?'\033[0m")   
                        print(f"\033[3m'Consider the following four sets.'\033[0m") 
                        scroll() 
 
                        print(f"\n\033[3m1: 'The set of all sets.'\033[0m")  
                        print(f"\033[3m2: 'The set of no things.'\033[0m")  
                        print(f"\033[3m3: 'The set of all sets that do not contain themselves.'\033[0m")  
                        print(f"\033[3m4: 'The set of all sets that contain themselves.'\033[0m")  
                        scroll() 


                        answer = input(f"\n\033[3m'Which of these are counterexamples to the claim, which is to say, which of these do not exist?\033[0m\n")
                        if answer != '1, 3':
                            print(f"\n\033[3m'Ah. I see.'\033[0m")
                            print(f"\033[3m'You have been guessing the answers.'\033[0m")
                            print(f"\033[3m'Naughty, naughty.'\033[0m")
                            scroll()

                            print(f"\n\033[3m'Now you die!'\033[0m")
                            scroll()

                            ready_check = ''
                            while ready_check != 'yes':
                                ready_check = input(f"\nThe Paradox Hunter is about to attack. Are you ready to face it?\n")
                            print(f"\nLet the battle commence!")

                            Fast_Battle(stats, attacks, Paradox_stats)
                            
                        

                        else: 
                            print(f"\nVale lets out a resounding cheer.")
                            print("He hoots, whoops, and raises his arms in the air.")
                            print("He very much cares.")
                            print("For the first time, the arrogant, balletic poise of the Hunter slips.")
                            print("A wave of relief blankets you.")
                            scroll()

                            print(f"\n\033[3m'Hmm. Yes. That is correct.'\033[0m")
                            print(f"\033[3m'You have answered all three questions correctly.'\033[0m")
                            print(f"\033[3m'You ... pass ... '\033[0m")
                            scroll()

                            print(f"\nVale throws his arm around you and cheers.")
                            print("He is rejuvinated, joyful.")
                            print("As are you.")
                            print("Russelian sighs, defeated ... for now.")
                            scroll()

                            print(f"\n\033[3m'I must let you live ... this time.'\033[0m") 
                            print(f"\033[3m'But we shall me again, you and I!' \033[0m") 
                            print(f"\033[3m'We will be watching you!!' \033[0m")
                            

                            print(f"\nAnd with that, the Hunter turns on it heel, and saunters away back into density of the forrest!")
                            scroll()


                            print(f"\n\033[3m***Stats Sidebar:\033[0m ")
    
                            print("\033[3mYou have gained 12 experience points.\033[0m")
                            stats["exp"] += 12  
                            stats["level"] += 2
                            stats["max_health"] += 2
                            stats["magical_strength"] += 2
                            stats["physical_strength"] += 2
                            stats["speed"] += 2
                            print(f"\033[3mYou have grown two levels. You are now level {stats['level']}.\033[0m ")
                            print("\033[3mYour stats have increased.\033[0m")
                            print ("\033[3mBack to the action!***\033[0m")
                            scroll() 


                            print(f"\n\033[3m***You have completed level 1, {Name}!\033[0m ")   
                            print("\033[3mWould you like to save the game?\033[0m ") 
                            print("\033[3mFair warning: if you don't, you won't be able to play level 2!***\033[0m ")
                            _ = 'y'
                            while _ != '':
                                _ = input(":::")

                            save = ''
                            while save != 'yes' and save != 'no':
                                save = input(f"\n\033[3m***So, would you like to save the game?***\033[0m\n")

                            if save == 'no':
                                print(f"\n\033[3m***I hope you enjoyed my level.***\033[0m ")

                            else: 
                                print(f"\n\033[3m***You have saved the game! On to level 2!***\033[0m ")
                                with open("Completion.csv", "w") as completion_file:
                                    completion_file.write("level 1,complete.") 
                                with open("Stats.csv", "w") as stats_file:
                                    for i in stats:
                                        stats_file.write(f"{i},{stats[i]}\n")
                                with open("Inventory.csv", "w") as inventory_file:
                                    for i in inventory:
                                        inventory_file.write(f"{i['item']['name']},{i['number']}\n")   
                                with open("Attacks.csv", "w") as attacks_file:
                                    for i in attacks:
                                        attacks_file.write(f"name,{i['name']}\n")


                    

              

elif action_check == "fight":
    if stats["speed"] > demon_stats["speed"]:
        answer = ''
        while answer != 'yes':
            answer = input(f"\nAre you ready???\n")
        
        print (f"\nLET THE BATTLE COMMENCE!")
        _ = input("__")  
        Fast_Battle(stats, attacks, demon_stats)  
         
    
    else:
        

        print(f"\nA potent, almost virulent, mixture of fear and excitement?? runs through you.")
        print("You take a deep breath, and steady yourself. ")    
        print("Let's do this!")
        _ = 'y'
        while _ != '':
            _ = input(":::")

        answer = ''
        while answer != 'yes':
            answer = input(f"\n\033[3m***Are you ready???***\033[0m\n")  
              
        
        print (f"\n***LET THE BATTLE COMMENCE!***")
        scroll()  
        Slow_Battle(stats, attacks, demon_stats)

        if stats["health"] > 0:
            scroll()
            print(f"\nThe demon takes an age to fall. ")
            print("When its bloated body is finally still on the forrest floor, you take a chasmically deep breath.")
            print("You did it. You are somehow still alive!!!")

            scroll()
        
            print(f"\n\033[3m***Stats Sidebar:\033[0m ")
    
            print("\033[3mYou have gained 5 experience points.\033[0m")
            stats["exp"] += 5  
            stats["level"] += 1
            stats["max_health"] += 1
            stats["magical_strength"] += 1
            stats["physical_strength"] += 1
            stats["speed"] += 1
            print(f"\033[3mYou have grown one level. You are now level {stats['level']}.\033[0m ")
            print("\033[3mYour stats have increased.\033[0m")
            print ("\033[3mBack to the action!***\033[0m")
            scroll() 
                

             
            print(f"\nYou collapse to the ground, as the river of adrenaline coursing through your veins begins to ebb.") 
            print("What the hell was that thing?")  
            print("And how did you fight so well? ")
            scroll()

            print(f"\nYour thoughts begin sprialling out of your grip. ")
            print("And just then you notice the old man gingergly poke his head out from behind a gnarled oak tree. ")
            print("His expression is hard to understand. ")
            print("You think perhaps it is a mix of sheer surprise and a giddy glee. ")
            _ = 'y'
            while _ != '':
                _ = input(":::")

            print(f"\n\033[3m'{Name}!!! That was incredible!!!'\033[0m ") 
            print(f"\033[3m'I thought when you didn't run, you were dead.'\033[0m ")
            print(f"\033[3m'But no!!! Amazing.'\033[0m ")
            print(f"\033[3m'Perhaps I am right about you afterall, {Name}.'\033[0m ")
            _ = 'y'
            while _ != '':
                _ = input(":::")

            print(f"\nEven amidst the bone-deep tiredness you feel a flash of anger, at this further vague, knowing suggestion.")
            print("You will need to find out what the old man knows.")
            print("Or what he thinks he knows!")    
            _ = 'y'
            while _ != '':
                _ = input(":::")

            print(f"\n\033[3m'Ah look. It seems there is an item poking out of the demon's pouch.'\033[0m ")
            print(f"\033[3m'Terrifying though they are, they do often have some very useful trinkets.'\033[0m ")
            print(f"\033[3m'Why don't you go see what it is?'\033[0m ")
            _ = 'y'
            while _ != '':
                _ = input(":::")

            print(f"\nYour internal ire momentarily interrupted, you slowly walk over to the demon's corpse." )
            print("There is indeed a vial of shiny, purple liquid poking out of the demon's pouch.")
            print("You very hesitantly reach in and remove the vial.") 
            _ = 'y'
            while _ != '':
                _ = input(":::")

            pick_up(Potion)

            _ = 'y'
            while _ != '':
                _ = input(":::")

            print(f"\nAs you place the potion in your backpack, you notice a scroll 'fragment' already in there. ")
            print(f"As with distressingly many things, you have no memory of this.")
            print(f"Perhaps there is some key to your past in there? Some clue?")
            print(f"You should ivestigate this later, you think.")
            _ = 'y'
            while _ != '':
                _ = input(":::")
        
            print(f"\n\033[3m***Item Tutprial:\033[0m")
            check = ''
            while check != 'yes' and check != 'no':
                check = input("\033[3mWould you like to check your inventory?***\033[0m\n")
            if check == "yes":    
                for i in inventory:
                    print(f"\n\033[3m***{i['item']['name']} :: {i['item']['description']} :: {i['number']}.***\033[0m")
                _ = 'y'
                while _ != '':
                    _ = input(":::")    

                print(f"\n\033[3m***The first slot is the name of the item.\033[0m ")
                print("\033[3mThe second is a description of the item.\033[0m ")
                print("\033[3mAnd the third is how many of the item you have.***\033[0m ")
                _ = 'y'
                while _ != '':
                    _ = input(":::")

                print(f"\n\033[3m***In future, if you would like to check your inventory, type 'items' when the '__' icon appears.\033[0m ")
                print(f"\033[3mIn future, if you would like to use an item from your inventory, type 'use' and the name of the item when the '__' icon appears.\033[0m ")
                print("\033[3mSo to use your potion, for instance, type in 'use potion' when the '__' icon appears.\033[0m ")
                print(f"\033[3mBack to the action!***\033[0m")
            
            else:
                print(f"\n\033[3m***An odd choice, {Name}.\033[0m")
                print(f"\033[3mBack to the action!***\033[0m")

            
            scroll()

            print(f"\nWithout any warning, the demon's body decays at an unnatural pace.")
            print("Its flesh dessicates, and its skeleton collapses.")
            print("One moment it is there.")
            print("And the next it is gone, in a puff of miasmic dust.")
            scroll()

            print(f"\nYou leap backwards, troubled!")
            print("For some reason this bothers you more than anything that has yet happened.")
            print("Things shouldn't be that sharp, you think.")
            print("Deeply troubled, you walk back over to the old man, who has keenly observed this puzzling interaction.")
            print("He belessedly silent on this point.")
            scroll()

            print(f"\n\033[3m'Always good to make use of what we find, eh?.'\033[0m ")
            print("\033[3m'I venture that potion would do you well!'\033[0m")
            print("\033[3m'Now, we need to get you out of the forrest.' \033[0m ")
            print("\033[3m'If that demon sensed you so quickly, there are likely several others nearby.'\033[0m ")
            print("\033[3m'And they may not be as cuddly as that one!'\033[0m ")
            scroll()

            print(f"\nAs soon as the disasterously prescient warning leaves the old man's lips, a demented cackle reverberates around the glade. ")
            print("A look base terror crowds his face.")
            print("You have a feeling that the cackler, whatever it is, is something you would rather avoid.")
            _ = 'y'
            while _ != '':
                _ = input(":::")


            print(f"\nThe old man's lips struggle to come unstuck. ")
            print("Before, he was fearful. Now, he is terrified.")
            print("Prising his lips apart, a Herculian effort, he finally manages to give words to his fear. ")
            _ = 'y'
            while _ != '':
                _ = input(":::")

            print(f"\n\033[3m'That is a Paradox Hunter.'\033[0m ")
            print("\033[3m'There is no time to explain.' \033[0m ")
            print("\033[3m'They are slow. But by the sounds of it, this one is closeby.'\033[0m ")
            print("\033[3m'If we run right now, we can escape it, and this forrest!'\033[0m ")
            print("\033[3m'Come with me, if you want to live!'\033[0m ")
            scroll()

            action_check = ''
            while action_check != 'run' and action_check != 'fight':
                action_check = input(f"\n\033[3m***The paradox hunter approaches. What will you do? Run, or fight?***\033[0m\n")
            
            if action_check == 'run':
                print(f"\nYou look at the expression on the old man's face, the pleading in his eyes.")
                print("And you nod, firmly.")
                print("He deeply breathes a sigh of relief.")
                _ = 'y'
                while _ != '':
                    _ = input(":::")

                print(f"\n\033[3mAway with us then!\033[0m ")
                print(f"\033[3mThere is no time to waste!\033[0m ")
                _ = 'y'
                while _ != '':
                    _ = input(":::")

                print(f"\nThe old man takes off at an almost manic pace.")
                print(f"And you are right there beside him!")


                _ = 'y'
                while _ != '':
                    _ = input(":::")
                
                print(f"\n\033[3m***Well done, {Name}!\033[0m ") 
                print(f"\033[3m***You have completed level 1.\033[0m ")   
                print("\033[3mWould you like to save the game?\033[0m ") 
                print("\033[3mFair warning: if you don't, you won't be able to play level 2!***\033[0m ")
                _ = 'y'
                while _ != '':
                    _ = input(":::")

                save = ''
                while save != 'yes' and save != 'no':
                    save = input(f"\n\033[3m***So, would you like to save the game?***\033[0m\n")

                if save == 'no':
                    print(f"\n\033[3m***I hope you enjoyed my level.***\033[0m ")

                else: 
                    print(f"\n\033[3m***You have saved the game! On to level 2!***\033[0m ")
                    with open("Completion.csv", "w") as completion_file:
                        completion_file.write("level 1,complete.") 
                    with open("Stats.csv", "w") as stats_file:
                        for i in stats:
                            stats_file.write(f"{i},{stats[i]}\n")
                    with open("Inventory.csv", "w") as inventory_file:
                        for i in inventory:
                            inventory_file.write(f"{i['item']['name']},{i['number']}\n")   
                    with open("Attacks.csv", "w") as attacks_file:
                        for i in attacks:
                            attacks_file.write(f"name,{i['name']}\n")
                           
                                   

            else: 
                print(f"\nYou look again at the expression on the old man's face, and the pleading in his eyes.")
                print("But from somewhere deep within you, resolve surges, oceanic in immensity.")
                print("You slowly shake your head. ")
                _ = 'y'
                while _ != '':
                    _ = input(":::")

                print(f"\nThe old man slumps.")
                print(f"As though he has just lost the last remnants of something essential.")
                _ = 'y'
                while _ != '':
                    _ = input(":::")

                print(f"\n\033[3m'Then we will die together.'\033[0m ")
                print(f"\033[3m'There is nothing left for me ...' \033[0m ")
                scroll()

                print(f"\nThe old man takes off his cloak.")
                print(f"And slowly turns to face the nightmare that has just entered the glade.")
                scroll()




                print(f"\nYou follow his gaze and lay your eyes on the Hunter.")
                print("Where the Enforcer had been bestial, gutteral, somatic, the Paradox Hunter is refined, understated, cerebral.")
                print("It strides into the glade, its movement languid, cocksure even. ")
                print("When its eyes come to rest on the old man, its aquiline face breaks into a full, toothy smile.")
                scroll()

                print(f"\n\033[3m'Vale ... What an unbridled pleasure it is to see you again.'\033[0m")
                print(f"\033[3m'It has been far too long.'\033[0m")
                scroll()

                print(f"\nFor a moment you wonder if the Hunter is speaking to you. Perhaps it knows you. Are you Vale?")
                print("But then you see its scarlet pupils are fixed firmly on the old man.")
                print("They simmer with recognition.")
                scroll()

                print(f"\n\033[3m'And which one are you again?'\033[0m")
                print(f"\033[3m'I never could tell you apart.'\033[0m")
                scroll()


                print(f"\nYou notice a momentary flicker of annoyance dance across the Hunter's face.")
                print("It flashes a razor sharp canine. ")
                print("And despite yourself, you feel your whole body wracked by an instinctual fear.")
                print("This, it transpires, is but a candle next to the bonfire that consumnes you when it suddenly turns and trains those scarlet pupils on you.")
                scroll()

                print(f"\n\033[3m'And who have we hear, Vale?'\033[0m")
                print(f"\033[3m'How have we not found them already?'\033[0m")
                print(f"\033[3m'They absolutley wreak of ... transgression.'\033[0m")
                scroll()

                print(f"\nYou have no idea what to say.")
                print("And even if you did, you are not sure you could manage a syllable, let alone a sentence.")
                scroll()


                print(f"\n\033[3m'Leave them alone, Russellian.'\033[0m")
                print(f"\033[3m'Whatever it is you want to settle, you can settle with me.'\033[0m")
                scroll()

                print(f"\nThe demon smiles even wider.")
                print("Gleeful at the tremor in Vale's voice.")
                scroll()

                print(f"\n\033[3m'Ah, you do you remember me, Vale.'\033[0m")
                print(f"\033[3m'How perfectly equisite.'\033[0m")
                print(f"\033[3m'Would that I could.'\033[0m")
                print(f"\033[3m'But you know just as well as I, that I can do no such thing.'\033[0m")
                print(f"\033[3m'This one will have to be tested.'\033[0m")
                print(f"\033[3m'There is nothing for it.'\033[0m")
                print(f"\033[3m'And if they fail ... Well, we'll none of us be long for this world.'\033[0m")
                scroll()

                print(f"\nRussellian turns to face you once again.")
                print("Cleary, it is revelling in its task. ")

                print(f"\n\033[3m'Now listen well. I am going to test you.'\033[0m")
                print(f"\033[3m'I am certain that you will fail.'\033[0m")
                print(f"\033[3m'But we must follow the rules, mustn't we?'\033[0m")
                print(f"\033[3m'I will ask you a series of three questions.'\033[0m")
                print(f"\033[3m'If you falter, you will face me in combat, and you will surely die.'\033[0m")
                scroll()

                print(f"\n\033[3m'The first two questions are yes/no.'\033[0m")
                print(f"\033[3m'Those are the only acceptable answers.'\033[0m")
                print(f"\033[3m'You had better choose wisely.'\033[0m")
                scroll()

                print(f"\n\033[3m'The third and final question, should you make it that far, is multiple choice.'\033[0m")
                print(f"\033[3m'There will be four options, named 1, 2, 3, and 4.'\033[0m")
                print(f"\033[3m'Give your answers to me as those numbers separated by commas and spaces.'\033[0m")
                print(f"\033[3m'So, for instance, if you think that 1 and 2 and 3 are correct answers, say '1, 2, 3'. '\033[0m")
                print(f"\033[3m'Good luck. You will need it.'\033[0m")
                scroll()



                ready_check = ''
                while ready_check != 'yes':
                    ready_check = input(f"\n\033[3m***Are you ready?***\033[0m\n")
                print(f"\nYou do not know what to expect.")
                print("What kind of questions does a demon ask?") 
                print("You take a moment to find your center.")
                print("You are about to find out!")  
                scroll()
                
                print(f"\nRussellian takes the sight of us in, and smiles wide.")
                print("Its whole is taught, entranced in its role.")
                print("At least one you is confident!")
                scroll()

                print(f"\n\033[3m'Now listen well old man.'\033[0m")
                print(f"\033[3m'Any help from you, even the slightest hint, and we all immediately die.'\033[0m")
                print(f"\033[3m'The integrity of the test is paramount!'\033[0m")
                print(f"\033[3m'Understood?'\033[0m") 
                scroll()

                print(f"\nYou look over at Vale.")
                print("He gives one, sharp nod. ")
                print("And remains silent.")
                print("You are on your own.")
                scroll()




                print(f"\n\033[3m'Fabulous!'\033[0m")
                print(f"\033[3m'Then here we go.'\033[0m")
                print(f"\033[3m'I, Rusellian, shall ask you some simple questions about the mathemaatics of set theory.'\033[0m")
                print(f"\033[3m'As everyone knows, a set is a mathematical object. It is an extensional collection of things, '\033[0m")
                print(f"\033[3m'i.e., a collection of things whose identity is determined purely by the identity of its members.'\033[0m")
                question_1 = ''
                while question_1 != 'yes' and question_1 != 'no':
                    question_1 = input(f"\n\033[3mQuestion 1: 'Is there an empty set -- a set which has no members?'\033[0m\n")
                if question_1 == 'no':
                    print(f"\n\033[3m'I knew it!'\033[0m")
                    print(f"\033[3m'I could smell it on you.'\033[0m")
                    print(f"\033[3m'Your whole being wreaks of it!'\033[0m")
                    scroll()

                    print(f"\n\033[3m'Of course there is!'\033[0m")
                    print(f"\033[3m'If there were not, how would anything work?!'\033[0m")
             
                    scroll()

                    print(f"\n\033[3m'Now you die!'\033[0m")
                    scroll()

                    ready_check = ''
                    while ready_check != 'yes':
                        ready_check = input(f"\nThe Paradox Hunter is about to attack. Are you ready to face it?\n")
                    print(f"\nLet the battle commence!")

                    Fast_Battle(stats, attacks, Paradox_stats)
                    


                else:
                    print(f"\n\033[3m'Hmm. Very good.'\033[0m")
                    print(f"\033[3m'Of course there is.'\033[0m")
                    print(f"\033[3m'If there were not, unmitigated chaos would ensue!'\033[0m")
                    print(f"\033[3m'On to the next question.'\033[0m")
                    scroll()

                    question_2 = ''
                    while question_2 != 'yes' and question_2 != 'no':
                        question_2 = input(f"\n\033[3mQuestion 2: 'Is it the case that for every property, there is a set of exactly those things which have that property?'\033[0m\n")
                    if question_2 == 'yes':
                        print(f"\n\033[3m'I knew it!'\033[0m")
                        print(f"\033[3m'I could smell it on you.'\033[0m")
                        print(f"\033[3m'Your whole being wreaks of it!'\033[0m")
                        scroll()

                        print(f"\n\033[3m'Of course there is not|!'\033[0m")
                        print(f"\033[3m'If there were then, there would be a set of all sets that do not contain themselves.'\033[0m")
                        print(f"\033[3m'And this set contains itself just in case it does not contain itself.'\033[0m")
                        print(f"\033[3m'A blatant, disgusting contradiction.'\033[0m")
                        scroll()

                        print(f"\n\033[3m'Now you die!'\033[0m")
                        scroll()

                        ready_check = ''
                        while ready_check != 'yes':
                            ready_check = input(f"\nThe Paradox Hunter is about to attack. Are you ready to face it?\n")
                        print(f"\nLet the battle commence!")

                        Fast_Battle(stats, attacks, Paradox_stats)    
                   
                

             
    
                    else:
                        print(f"\n\033[3m'Again, very good. Of course it's not the case.'\033[0m")
                        print(f"\033[3m'It is a preposterous, pernicious, paradoxical proposition!'\033[0m")  
                        print(f"\033[3m'A crutch for the naieve of mind and heart.'\033[0m")
                        scroll()
                        
                        print(f"\n\033[3m'But do you know why?'\033[0m")   
                        print(f"\033[3m'Consider the following four sets.'\033[0m") 
                        scroll() 
 
                        print(f"\n\033[3m1: 'The set of all sets.'\033[0m")  
                        print(f"\033[3m2: 'The set of no things.'\033[0m")  
                        print(f"\033[3m3: 'The set of all sets that do not contain themselves.'\033[0m")  
                        print(f"\033[3m4: 'The set of all sets that contain themselves.'\033[0m")  
                        scroll() 


                        answer = input(f"\n\033[3m'Which of these are counterexamples to the claim, which is to say, which of these do not exist?\033[0m\n")
                        if answer != '1, 3':
                            print(f"\n\033[3m'Ah. I see.'\033[0m")
                            print(f"\033[3m'You have been guessing the answers.'\033[0m")
                            print(f"\033[3m'Naughty, naughty.'\033[0m")
                            scroll()

                            print(f"\n\033[3m'Now you die!'\033[0m")
                            scroll()

                            ready_check = ''
                            while ready_check != 'yes':
                                ready_check = input(f"\nThe Paradox Hunter is about to attack. Are you ready to face it?\n")
                            print(f"\nLet the battle commence!")

                            Fast_Battle(stats, attacks, Paradox_stats)
                            
                        

                        else: 
                            print(f"\nVale lets out a resounding cheer.")
                            print("He hoots, whoops, and raises his arms in the air.")
                            print("He very much cares.")
                            print("For the first time, the arrogant, balletic poise of the Hunter slips.")
                            print("A wave of relief blankets you.")
                            scroll()

                            print(f"\n\033[3m'Hmm. Yes. That is correct.'\033[0m")
                            print(f"\033[3m'You have answered all three questions correctly.'\033[0m")
                            print(f"\033[3m'You ... pass ... '\033[0m")
                            scroll()

                            print(f"\nVale throws his arm around you and cheers.")
                            print("He is rejuvinated, joyful.")
                            print("As are you.")
                            print("Russelian sighs, defeated ... for now.")
                            scroll()

                            print(f"\n\033[3m'I must let you live ... this time.'\033[0m") 
                            print(f"\033[3m'But we shall me again, you and I!' \033[0m") 
                            print(f"\033[3m'We will be watching you!!' \033[0m")
                            

                            print(f"\nAnd with that, the Hunter turns on it heel, and saunters away back into density of the forrest!")
                            scroll()


                            print(f"\n\033[3m***Stats Sidebar:\033[0m ")
    
                            print("\033[3mYou have gained 12 experience points.\033[0m")
                            stats["exp"] += 12  
                            stats["level"] += 2
                            stats["max_health"] += 2
                            stats["magical_strength"] += 2
                            stats["physical_strength"] += 2
                            stats["speed"] += 2
                            print(f"\033[3mYou have grown two levels. You are now level {stats['level']}.\033[0m ")
                            print("\033[3mYour stats have increased.\033[0m")
                            print ("\033[3mBack to the action!***\033[0m")
                            scroll() 


                            print(f"\n\033[3m***You have completed level 1, {Name}!\033[0m ")   
                            print("\033[3mWould you like to save the game?\033[0m ") 
                            print("\033[3mFair warning: if you don't, you won't be able to play level 2!***\033[0m ")
                            _ = 'y'
                            while _ != '':
                                _ = input(":::")

                            save = ''
                            while save != 'yes' and save != 'no':
                                save = input(f"\n\033[3m***So, would you like to save the game?***\033[0m\n")

                            if save == 'no':
                                print(f"\n\033[3m***I hope you enjoyed my level.***\033[0m ")

                            else: 
                                
                                print(f"\n\033[3m***You have saved the game! On to level 2!***\033[0m ")
                                with open("Completion.csv", "w") as completion_file:
                                    completion_file.write("level 1,complete.") 
                                with open("Stats.csv", "w") as stats_file:
                                    for i in stats:
                                         stats_file.write(f"{i},{stats[i]}\n")
                                with open("Inventory.csv", "w") as inventory_file:
                                    for i in inventory:
                                        inventory_file.write(f"{i['item']['name']},{i['number']}\n")   
                                with open("Attacks.csv", "w") as attacks_file:
                                    for i in attacks:
                                        attacks_file.write(f"name,{i['name']}\n")
                                

                