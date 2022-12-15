name = input("What's your name?")

def start():
    print("")
    print("Welcome to the forests of Avalon", name,"!")
    print("")
    pickWeapon()

def pickWeapon():
    global weaponChoice
    print("")
    weaponChoice = input("You have fallen through the purple swiriling wormhole of Avalon and have found yourself back in the Babylon Jungle. Home to some of the most deadly creatures on the planet. As you dust yourself off from your abrupt wormhole suck and begin to get your bearings you pick up your weapon. What was your weapon, again? (sword, shield, magic wand)")
    if weaponChoice == "sword" or weaponChoice == "shield" or weaponChoice == "magic wand":
        print("")
        print("Oh right! You fight with a", weaponChoice, "!")
    else:
        print("Sorry, I didn't catch that, what is your weapon again?")
        print("")
        pickWeapon()
    hearNoise()

def hearNoise():
    print("")
    noiseChoice = input("You get your mind in order, put your " + weaponChoice + " on your belt and brush the dust off your cap. As you stand up you hear a rustling in the bushes behind you. Do you want to investigate it or run away?(investigate/run)")
    if noiseChoice == "investigate":
        print("")
        gnome()
    elif noiseChoice =="run":
        print("")
        print("Your cowardice has gotten the best of you. You turn in the opposite direction and run into the darkness toward a small firelight you see off in the distance.")
        print("")
        firelight()
    else:
        print("Sorry, I didn't catch that, what is your answer again?")
        print("")
        hearNoise()

def gnome():
    global gnomeChoice
    print("")
    gnomeChoice = input("You go peer behind the bushes and find a small baby gnome wrapped in a red blanket. He looks up at you and giggles. Cute little defenseless fella. Can't be safe around here for him. Should you take him with you or leave him behind? (take him/ leave him)")
    if gnomeChoice == "take him":
        print("")
        print("You listened to your heart and decided to take the baby gnome with you. You tie him to your back and carry on down the path. You head north-- as you recall a small town from your previous visit-- which has a wormhole of their own that you can take home. On the way, through the darkness- you see a campfire light. You figure perhaps the people there can help you figure out which direction the town is in.")
        firelight()
    elif gnomeChoice == "leave him":
        print("")
        print("You decided to leave the gnome. You can't find your way out of here while worrying about a baby gnome. Besides, I'm sure his mother will be back for him in a moment. Like a deer. As you turn around you see a campfire off in the distance. You find yourself absolutely mezmerized by it. You head towards the fire.")
        firelight()

def firelight():
    print("")
    fireChoice = input("As you get close to the firelight, something seems strange. The fire begins to burst into different colored light, and you see figures around the fire chanting something in a strange tongue you've never heard before. They begin to beat a large drum and you can see them carrying out what seems to be a sacrifice. They begin to tie what looks like a young child above the fire. Should you cause a distraction and possibly save the child or sneak away?(distract/sneak away)")
    if fireChoice == "distract":
        print("")
        if gnomeChoice == "take him":
            print("")
            print("You tighten the baby gnome on your back and take out your " + weaponChoice  +" You jump on top of one of the stumps around the fire and swing your " + weaponChoice + " at one of the big guys nearby." )




start()