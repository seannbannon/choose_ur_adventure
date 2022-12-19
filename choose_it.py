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
        print("Oh right! You fight with a", weaponChoice + "!")
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
    else:
        print("Sorry, I didn't catch that, what is your answer again?")
        print("")
        gnome()

def firelight():
    print("")
    fireChoice = input("As you get close to the firelight, something seems strange. The fire begins to burst into different colored light, and you see figures around the fire chanting something in a strange tongue you've never heard before. They begin to beat a large drum and you can see them carrying out what seems to be a sacrifice. They begin to tie what looks like a young child above the fire. Should you try to save the child or sneak away?(save/sneak away)")
    if fireChoice == "save":
        print("")
        if gnomeChoice == "take him":
            print("")
            print("You tighten the baby gnome on your back and take out your " + weaponChoice + ".")
            battlescene()
        if gnomeChoice == "leave him":
            print("")
            print("This must be why that baby gnome was in the bushes. Someone hid it there to avoid it being used as a human sacrifice.")
            battlescene()
    if fireChoice == "sneak away":
        print("")
        print("You decide it would probably be best to let sleeping dogs lie. You pull up your hood and creep through the shadows to avoid detection. You feel bad for leaving that child to die, and you should. However, it's not up to you to save the world. You aren't entirely sure how you even got here and you're focused on making it back home in one piece. You are a coward, though, and def do not have what it takes to be a great adventurer.")
        quicksand()
    else:
        print("Sorry, I didn't catch that, what is your answer again?")
        print("")
        firelight()

def battlescene():
    print("")
    print("You jump on top of one of the stumps around the fire and swing your " + weaponChoice + " at one of the big guys nearby.")
    if weaponChoice == "sword":
        print("")
        print("You manage to slice the cheek of one of the largest elves. He is unphased and pissed off. He leaps at you- blood flooding from his sunken face- and you thrust your sword deep into his thigh. He goes down and lets out a mighty yell. Everyone freezes. Clearly they have a mighty warrior before them. They wait for you to speak.")
    if weaponChoice == "magic wand":
        print("")
        print("A bolt of lightening flies from your wand- strinking the boss elf between the eyes. He does down hard. Everyone freezes. They have't seen a wizard in over 400 years. They wait for you to to speak.")
    if weaponChoice == "shield":
        print("")
        print("You smash the face of the largest elf. He falls backwards into the fire. Another one charges you from behind, knocking you down. He jumps on top of you, but you manage to push him off with your shield. You scuffle up to your feet and thrust the bottom of the shield into the elf's throat. Decapitating him. Everyone halts and stares at you. They wait for you to say something.")

def quicksand():
    print("")
    quicksandChoice = input("As you sneak past the fire- you step into what seems to be very thick mud. You trudge ahead but find yourself hopelessly sinking deeper into the mud. Wait a minute. This isn't regular mud. This is quicksand! Before you realize it you are up to your waist. You reach for a nearby branch but it is just out of reach. Your only hope is to yell for help and hope that the people around the fire hear you and help you. But they are clearly savages. Do you yell for help or accept your inevitable fate to suffocate in the sand? (yell/die)")
    if quicksandChoice == "yell":
        print("")
        print("You scream for help over and over. You truly are a coward. You can hear the savages getting closer to you. Next thing you know you are up to your neck in quicksand and the savages finally arrive. Oh thank goodness. You plead for them to help you out of the quicksand. You say something about how much you hate babies and love buring them alive. They speak in some kind of caveman sounding tongue. The begin to pick up large stones and one after another begin throwing them at your cranium. You regret your decision to yell. They kill you. Your body slowly sinks into the quicksand, where it stays for the next 27 million years. You are dead.")
        if gnomeChoice == "take him":
            print("")
            print("The baby gnome on your back died too. Way to go.")
    if quicksandChoice == "die":
        print("")
        print("You accept your fate. You hear the birds chirping in the trees. You see the sun setting off in the distance. The sky an orange-pink. You see how fortunate you were to have been alive at all. After a couple of minutes you're up to your neck in quicksand. You feel how good it is to just take a deep breath. Your mouth and nose go under the quicksand. You try to breathe but just feel a heaviness. Everything goes black. The next thing you know you awaken next to your spouse of 27 years. You grab her and kiss her cheek. You go downstairs to heat up a pot of tea.")
    else:
        print("Sorry, I didn't catch that, what is your answer again?")
        print("")
        quicksand()



def speech():
    print("")
    speechChoice = input("You jump up on a nearby wooden table and prepare for you speech. You're unsure if you should try to convince them of the error of their ways or if you should trick them and make them think you are on their side? (convince/trick)")
    if speechChoice == "convince":
        print("")
        print("You begin by addressing the crowd and telling them how sacred life it. How they are acting barbarically and how there is no possible way that ")

start()