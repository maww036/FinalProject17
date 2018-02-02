import time
import sys

def print_slow(str):
   """prints the text letter by letter"""
   for letters in str:
       sys.stdout.write(letters)
       sys.stdout.flush()
       time.sleep(.06)

print_slow("Welcome to A Mermaid Tale: The Game! Please answer these questions before starting the game.\n")

name = input("\nWhat is your name? ").upper()
age = input("\nHow old are you? ")
gender = input("\nWhat do you identify as? ").lower()

print("""\nWelcome""", name,"""to the start of the game! You are a""", age,"""year-old""", gender,"""with a passion for surfing
You have recently just found out that you are the long lost mermaid royal of Oceana! With the help of Zuma,
your trusty pink dolphin, you will go on an adventure to rescue your mother from your wicked aunt, Eris, and return
Oceana to the beauty it once had!""")

print_slow("\nBefore you start your adventure, you have to obtain a tail so that you can disguise yourself and hide from your aunt.\n")

print_slow("\nLuckily Zuma knows two places where you can get the perfect tail.\n")

class Shopping():
    def __init__(self, store, description):
        self.store = store
        self.description = description

store_a = ("\nStore A: H&Fin,a high-end boutique that sells the latest and most fashionable tails to the most latest and fasionable people of Oceana!\n")
store_b = ("\nStore B: Finever 21,an affordable tail shop that sells the latest trends for our teen swimmers in Oceana!\n")

print_slow(store_a)
print_slow(store_b)

x = "invalid"
while x == "invalid":
    answer = input("\nPlease choose which store you would like to go to: ")
    if answer == "a":
        print_slow("You chose store A, H&Fin. Great choice!")
        x = "valid"
    elif answer == "b":
        print_slow("You chose store B, Finever 21. Great choice!")
        x = "valid"
    else:
        print_slow("That is an invalid choice please try again!")
        x = "invalid"

print_slow("\nYou and Zuma enter the store and spot two of her mermaid friends, Kayla and Xylie.")
print_slow("They are shocked to see a human in the city of Oceana but they agree to help on your adventure\n")
print_slow("'We should go to the Destinies and see if they have any advice for us!' Kayla says to you\n")
print_slow("'The Destinies?', you ask\n")
print_slow("'Yea! They can see in to the fuuuuture!' Xylie comments as she wiggles her fingers around to emphasize her point\n")
print_slow("'Maybe they will be able to tell us what we need to find in order to defeat Eris once and for all!', you exclaim loudly\n")
print_slow("'Yea!' they group cheers as they imagine the city going back to how it was before Eris took control over everything. With all that excitement, you had almost forgot the real reason why you came to the store.")

class Polite():
    def __init__(self, option, description):
        self.option = option
        self.description = description

option_1 = ("\nOption 1: 'Hey, would it be alright if I try on some tails?'")
option_2 = ("\nOption 2: 'Can you hurry up and bring me a tail? I don't have all day to just sit around!'")

print_slow(option_1)
print_slow(option_2)

x = "invalid"
while x == "invalid":
    answer = input("\nPlease choose an option: ")
    if answer == "1":
        print("""\n'Absolutely  positively! I think I have the perfect one just for you!' Xylie exclaimesas she runs to the
back of the store to get the "perfect tail" She comes back out with a light blue colored tail. You put it on and swim
around to get used to your new way of transportation. """)
        x = "valid"
    elif answer == "2":
        print_slow("\nOof! You made Kayla and Xylie angry due to your rudeness. They refuse to give you a tail and you are son captured by Eris.\nGAME OVER!!!!")
        x = "valid"
    else:
        print_slow("That is an invalid choice please try again!")
        x = "invalid"

print_slow("""After becoming comfortable with your new tail, you and the gang head out to meet the Destinies. When you get your
destination, you spot Eris walking out of the Destinies!""")

class Hide():
    def __init__(self, option, direction):
        self.option = option
        self.direction = direction

option_1 = ("\nOption 1: Go left.")
option_2 = ("\nOption 2: Go right.")
option_3 = ("\nOption 3: Go up.")

print_slow(option_1)
print_slow(option_2)
print_slow(option_3)

x = "invalid"
while x == "invalid":
    answer = input("\nPlease choose an option: ")
    if answer == "1":
        print_slow("\nOh no! One of Eris' minions saw you and captured you and your friends before you could try and swim away.\nGAME OVER!!!!")
        x = "valid"
    elif answer == "2":
        print_slow("\nOh no! One of Eris' minions saw you and captured you and your friends before you could try and swim away.\nGAME OVER!!!!")
        x = "valid"
    elif answer == "3":
        print_slow("\nGreat job! You weren't seen by anyone and Eris and her minions left the Destinies without a single clue of you being here.")
        x = "valid"
    else:
        print_slow("That is an invalid choice please try again!")
        x = "invalid"

print_slow("""You enter the Destinies and they tell you that to defeat your aunt you have to collect three items. You have to get:\n
1. The celestial comb\n2. A dream fish\n3. Your aunt's protective necklace.""")

print_slow("""You decide to go after the celestial comb first since its located in an underwater cove close by. As you and the rest of the gang get closer
to the cove you notice three huge jellyfish guarding the cove. How will you lead them away from the cove?""")

class Hide():
    def __init__(self, option, direction):
        self.option = option
        self.direction = direction

option_1 = ("\nOption 1: Go right up to the jellyfish and ask.")
option_2 = ("\nOption 2: Distract the jellyfish and sneak in.")
option_3 = ("\nOption 3: Go right into the cove like you're the boss.")

print_slow(option_1)
print_slow(option_2)
print_slow(option_3)

x = "invalid"
while x == "invalid":
    answer = input("\nPlease choose an option: ")
    if answer == "1":
        print_slow("\nOh no! Your distraction didn't work and the jellyfish electrified you!\n GAME OVER!!!")
        x = "valid"
    elif answer == "2":
        print_slow("\nGreat job! You were able to guide the jellyfish away and obtain the celestial comb. On to the next!")
        x = "valid"
    elif answer == "3":
        print_slow("\nOh no! Your distraction didn't work and the jellyfish electrified you!\n GAME OVER!!!")
        x = "valid"
    else:
        print_slow("That is an invalid choice please try again!")
        x = "invalid"

print_slow("Thanks for tryin this preview of the game. Hope you liked it.")