name = input("What is your name? ").upper()
age = input("How old are you? ")
gender = input("Are you a boy or a girl? ").lower()
sea_animal = input("Pick a sea animal. ").lower()
animal_name = input("Pick a name for your sea creature. ")

print("""Welcome""", name,"""to the start of the game! You are a""" ,age, """year-old""", gender, """with a passion for surfing! You have
recently just found out that you are the long lost mermaid princess of Oceana! With the help of""", animal_name,""", your trusty""", sea_animal,
""", you will go on an adventure to rescue your mother from your wicked aunt and return Oceana to the beauty it once had!""")

print("""\nBefore you start your adventure, you have to obtain a tail so that you can disguise yourself and hide from your aunt. Luckily""",
animal_name, """knows two places where you can get the perfect tail.""")

class Shopping():
    def __init__(self, store, description):
        self.store = store
        self.description = description

store_a = ("H&Fin", "A high-end boutique that sells the latest and most fashionable tails to the most least and fasionable people of Oceana!")
store_b = ("Finever 21", "An affordable tail shop that sells the latest trends for our teen swimmers in Oceana!")

print(store_a)
print(store_b)

answer = input("Please choose which store you would like to go to: ")
if answer in ("a","b"):
    if answer != "a":
        print("You chose store B, Finever 21. Great choice!")
    if answer == "a":
        print("You chose store A, H&Fin. Great choice!")

#while player_response !=