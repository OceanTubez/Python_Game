"""
Game_ProtoType

Description:

This is a Beta Game: QuizCrate
In works.

COPYRIGHT @2021

OceanTubez Inc.
"""
# ----// Importing Important Modules/Variables \\---- #
import random

# Printing Version and Valid ID #

print("V. 1.3.2")

ValidID_Checker = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
ValidID_Checker2 = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
ValidID_Checker3 = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
ValidID_Checker4 = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

ValidID = ValidID_Checker + ValidID_Checker2 + ValidID_Checker3 + ValidID_Checker4
print("ValidID:",ValidID,)

# Printed Version and ValidID #


Inventory = ""
Money = 0
# ----// Imported Modules/Variables \\---- #

# --// Code Starts \\-- #
print("Money: ",Money,)
print("Inventory:",Inventory,)

print("Answer these questions corrrectly to get more Money!")

Question_1 = input("Who is the president of The United States of America right now?")
if Question_1 == "Joe Biden":
    print("Correct! You earned $100 this round.")
    Money = (Money + 100)
    print("Money:",Money,)
else:
    print("Wrong Answer! The Answer is Joe Biden!")

Question_2 = input("What is the tallest animal on earth?")
if Question_2 == "Giraffe":
    print("Correct! You earned $20 this round.")
    Money = (Money + 20)
    print("Money:",Money,)
else:
    print("Wrong Answer! The Answer is Giraffe!")
    print("Now onwards, you will lose money for getting questions wrong. Money lost is half of money earned that question.")
    Money = (Money - 10)
    print("Money:",Money,)

print("Every 2 questions, We will ask you if you want to buy a crate from our store.")
print("These crate's can be opened for prizes which can be sold, or you can wish to keep them.")
ShopChung = input("Would you like to access the shop? Answer in Yes/No only.")
if ShopChung == "Yes":
    print("Welcome to the shop!")
    print("Here you can buy Crates! There are 5 types.")
    print("Common, Uncommon, Rare, Epic, and Legendary.")
    print("You can buy the UNI-CRATE, which contains all these items, and you will get one out of random.")
    print("Or you can get Individual crates, which only include 2-3 Categories of items.")
    print("Crate codes:")
    print("Common - Rare(CR): $20, Rare - Legendary(RL): $120, Rare - Epic(RE): $70")
    ChoiceChung = input("Which crate would you like to buy? [CR, RL, RE, UNI]")
    if ChoiceChung == "CR":
        if Money >= 20:
            print("Chosen Crate to open: Common - Rare")
            Money = (Money - 20)
            ItemRad = random.choice(["Common Red Capsule", "Common Red Capsule", "Common Red Capsule", "Common Blue Capsule", "Common Blue Capsule", "Common Blue Capsule", "Common Blue Capsule", "Common Green Capsule", "Common Green Capsule", "Common Green Capsule", "Uncommon Neon-Red Capsule", "Uncommon Neon-Red Capsule", "Uncommon Neon-Green Capsule", "Uncommon Neon-Green Capsule", "Uncommon Neon-Blue Capsule", "Uncommon Neon-Blue Capsule", "Rare Glow-Red Capsule", "Rare Glow-Green Capsule", "Rare Glow-Blue Capsule"])
            print("Unboxed:",ItemRad,)
            print("Money:",Money,)
            Inventory = ("Inventory:",Inventory,ItemRad,)
            print(Inventory)
        else:
            print("You don't have enough money to buy this crate, please access the shop next time.")
    if ChoiceChung == "RE":
        if Money >= 70:
            print("Chosen Crate to open: Rare - Epic")
            Money = (Money - 70)
            ItemRad = random.choice(["Rare Glow-Red Capsule", "Rare Glow-Red Capsule", "Rare Glow-Green Capsule", "Rare Glow-Green Capsule", "Rare Glow-Blue Capsule", "Rare Glow-Blue Capsule", "Epic Glitter-Red Capsule", "Epic Glitter-Blue Capsule", "Epic Glitter-Green Capsule"])
            print("Unboxed:",ItemRad,)
            print("Money:",Money,)
            Inventory = ("Inventory:",Inventory,ItemRad,)
            print(Inventory)
        else:
            print("You don't have enough money to buy this crate, please access the shop next time.")
    if ChoiceChung == "UNI":
        if Money >= 60:
            print("Chosen Crate to open: Universal")
            Money = (Money - 60)
            ItemRad = random.choice(["Common Red Capsule", "Common Red Capsule", "Common Red Capsule", "Common Blue Capsule", "Common Blue Capsule", "Common Blue Capsule", "Common Blue Capsule", "Common Green Capsule", "Common Green Capsule", "Common Green Capsule", "Uncommon Neon-Red Capsule", "Uncommon Neon-Red Capsule", "Uncommon Neon-Green Capsule", "Uncommon Neon-Green Capsule", "Uncommon Neon-Blue Capsule", "Uncommon Neon-Blue Capsule", "Rare Glow-Red Capsule", "Rare Glow-Green Capsule", "Rare Glow-Blue Capsule", "Epic Glitter-Red Capsule", "Epic Glitter-Blue Capsule", "Epic Glitter-Green Capsule", "Legendary RadioActive-Red Capsule", "Legendary RadioActive-Blue Capsule", "Legendary RadioActive-Green Capsule"])
            print("Unboxed:",ItemRad,)
            print("Money:",Money,)
            Inventory = ("Inventory:",Inventory,ItemRad,)
            print(Inventory)
        else:
            print("You don't have enough money to buy this crate, please access the shop next time.")
    if ChoiceChung == "RL":
        if Money >= 120:
            print("Chosen Crate to open: Rare - Legendary")
            Money = (Money - 120)
            ItemRad = random.choice(["Rare Glow-Red Capsule", "Rare Glow-Green Capsule", "Rare Glow-Blue Capsule", "Epic Glitter-Red Capsule", "Epic Glitter-Blue Capsule", "Epic Glitter-Green Capsule", "Legendary RadioActive-Red Capsule", "Legendary RadioActive-Blue Capsule", "Legendary RadioActive-Green Capsule"])
            print("Money:",Money,)
            Inventory = ("Inventory:",Inventory,ItemRad,)
            print(Inventory)
        else:
            print("You don't have enough money to buy this crate, please access the shop next time.")
else:
    print("Alright then, Lets continue on!")

Question_3 = input("What is Python?")
if Question_3 == "A programming language":
    print("Correct! You earned $50 this round.")
    Money = (Money + 50)
    print("Money:",Money,)
else:
    print("Wrong Answer! The Answer is A programming language!")
    print("You lost $25!")
    Money = (Money - 25)
    print("Money:",Money,)

Question_4 = input("Which FreeFire Update is coming out next? ")
if Question_4 == "OB30 Update":
    print("Correct! You earned $100 this round.")
    Money = (Money + 100)
    print("Money:",Money,)
else:
    print("Wrong Answer! The Answer is OB30 Update")
    print("You lost $50!")
    Money = (Money - 25)
    print("Money:",Money,)

ShopChung = input("Would you like to access the shop? Answer in Yes/No only.")
if ShopChung == "Yes":
    print("Welcome to the shop!")
    print("Here you can buy Crates! There are 5 types.")
    print("Common, Uncommon, Rare, Epic, and Legendary.")
    print("You can buy the UNI-CRATE, which contains all these items, and you will get one out of random.")
    print("Or you can get Individual crates, which only include 2-3 Categories of items.")
    print("Crate codes:")
    print("Common - Rare(CR): $20, Rare - Legendary(RL): $120, Rare - Epic(RE): $70")
    ChoiceChung = input("Which crate would you like to buy? [CR, RL, RE, UNI]")
    if ChoiceChung == "CR":
        if Money >= 20:
            print("Chosen Crate to open: Common - Rare")
            Money = (Money - 20)
            ItemRad = random.choice(["Common Red Capsule", "Common Red Capsule", "Common Red Capsule", "Common Blue Capsule", "Common Blue Capsule", "Common Blue Capsule", "Common Blue Capsule", "Common Green Capsule", "Common Green Capsule", "Common Green Capsule", "Uncommon Neon-Red Capsule", "Uncommon Neon-Red Capsule", "Uncommon Neon-Green Capsule", "Uncommon Neon-Green Capsule", "Uncommon Neon-Blue Capsule", "Uncommon Neon-Blue Capsule", "Rare Glow-Red Capsule", "Rare Glow-Green Capsule", "Rare Glow-Blue Capsule"])
            print("Unboxed:",ItemRad,)
            print("Money:",Money,)
            Inventory = ("Inventory:",Inventory,ItemRad,)
            print(Inventory)
        else:
            print("You don't have enough money to buy this crate, please access the shop next time.")
    if ChoiceChung == "RE":
        if Money >= 70:
            print("Chosen Crate to open: Rare - Epic")
            Money = (Money - 70)
            ItemRad = random.choice(["Rare Glow-Red Capsule", "Rare Glow-Red Capsule", "Rare Glow-Green Capsule", "Rare Glow-Green Capsule", "Rare Glow-Blue Capsule", "Rare Glow-Blue Capsule", "Epic Glitter-Red Capsule", "Epic Glitter-Blue Capsule", "Epic Glitter-Green Capsule"])
            print("Unboxed:",ItemRad,)
            print("Money:",Money,)
            Inventory = ("Inventory:",Inventory,ItemRad,)
            print(Inventory)
        else:
            print("You don't have enough money to buy this crate, please access the shop next time.")
    if ChoiceChung == "UNI":
        if Money >= 60:
            print("Chosen Crate to open: Universal")
            Money = (Money - 60)
            ItemRad = random.choice(["Common Red Capsule", "Common Red Capsule", "Common Red Capsule", "Common Blue Capsule", "Common Blue Capsule", "Common Blue Capsule", "Common Blue Capsule", "Common Green Capsule", "Common Green Capsule", "Common Green Capsule", "Uncommon Neon-Red Capsule", "Uncommon Neon-Red Capsule", "Uncommon Neon-Green Capsule", "Uncommon Neon-Green Capsule", "Uncommon Neon-Blue Capsule", "Uncommon Neon-Blue Capsule", "Rare Glow-Red Capsule", "Rare Glow-Green Capsule", "Rare Glow-Blue Capsule", "Epic Glitter-Red Capsule", "Epic Glitter-Blue Capsule", "Epic Glitter-Green Capsule", "Legendary RadioActive-Red Capsule", "Legendary RadioActive-Blue Capsule", "Legendary RadioActive-Green Capsule"])
            print("Unboxed:",ItemRad,)
            print("Money:",Money,)
            Inventory = ("Inventory:",Inventory,ItemRad,)
            print(Inventory)
        else:
            print("You don't have enough money to buy this crate, please access the shop next time.")
    if ChoiceChung == "RL":
        if Money >= 120:
            print("Chosen Crate to open: Rare - Legendary")
            Money = (Money - 120)
            ItemRad = random.choice(["Rare Glow-Red Capsule", "Rare Glow-Green Capsule", "Rare Glow-Blue Capsule", "Epic Glitter-Red Capsule", "Epic Glitter-Blue Capsule", "Epic Glitter-Green Capsule", "Legendary RadioActive-Red Capsule", "Legendary RadioActive-Blue Capsule", "Legendary RadioActive-Green Capsule"])
            print("Money:",Money,)
            Inventory = ("Inventory:",Inventory,ItemRad,)
            print(Inventory)
        else:
            print("You don't have enough money to buy this crate, please access the shop next time.")
else:
    print("Alright then, Lets continue on!")
# --// Code Ends \\-- #
