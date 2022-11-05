name = input("What's your name?")
print("Welcome to the forests of Avalon", name,"!")

answer = input(
    "You have fallen through the purple swiriling wormhole of Avalon and have found yourself back in the Babylon Jungle. Home to some of the most deadly creatures on the planet. As you dust yourself off from your abrupt wormhole suck and begin to get your bearings you pick up your weapon. What was your weapon, again? (sword, shield, magic wand)").lower()


if answer == "sword" or "shield" or "magic wand":
    print(f'Oh, right! You fight with a {answer}!')
else:
    print("Sorry, I didn't catch that. What was your weapon again?")

