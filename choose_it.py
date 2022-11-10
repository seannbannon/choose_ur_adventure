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
        # print("You go peer behind the bushes and find a small baby gnome wrapped in a red blanket. He looks up at you and giggles. Cute little defenseless fella. Can't be safe around here for him. Should you take him with you or leave him behind? (take him/ leave him)")
        gnome()
    elif noiseChoice =="run":
        print("Your cowardice has gotten the best of you. You turn in the opposite direction and run into the darkness toward a small firelight you see off in the distance.")
    else:
        print("Sorry, I didn't catch that, what is your answer again?")
        print("")
        hearNoise()

def gnome():
    print("")
    gnomeChoice = input("You go peer behind the bushes and find a small baby gnome wrapped in a red blanket. He looks up at you and giggles. Cute little defenseless fella. Can't be safe around here for him. Should you take him with you or leave him behind? (take him/ leave him)")
    if gnomeChoice == "take him":
        print("")
        print("You listened to your heart and decided to take the baby gnome with you. You tie him to your back and carry on down the path. You head north-- as you recall a small town from your previous visit-- which has a wormhole of their own that you can take home. ")


start()







# weapon = input(
#     "You have fallen through the purple swiriling wormhole of Avalon and have found yourself back in the Babylon Jungle. Home to some of the most deadly creatures on the planet. As you dust yourself off from your abrupt wormhole suck and begin to get your bearings you pick up your weapon. What was your weapon, again? (sword, shield, magic wand)").lower()


# if weapon == ("sword" or "shield" or "magic wand"):
#     print(f'Oh, right! You fight with a {weapon}!')
# else:
#     print("Sorry, I didn't catch that. What was your weapon again?")

