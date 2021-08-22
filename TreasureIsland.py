print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = input("You are on the middle of an island. You only have two ways to go, Left or Right. Where do you want to go? ")
if choice1 == "left" or choice1 == "LEFT" or choice1 == "Left":
    print("You arrived at an old dockyard. Looks like someone lives here and makes his living by doing fishing.\n")
    choice2=input("Do you want to wait for the fisherman or swim forward? ")
    if choice2 == "yes" or choice2 == "YES" == choice2 == "Yes":
        print("Thank God!! He was a good man and he was carrying a boat. Now he gave you a lift to an island. It's too dark here but you are close to your treasure and you can't give up now. \n")
        choice3=input("There are 3 doors in front of you - Red, Yellow and Blue. The treasure is on the other side of one of these doors but if you pick the wong door you die. ")
        if choice3 == "Yellow" or choice3 == "YELLOW" or choice3 == "yellow":
            print("Congrats!! You won the game and the treasure is all yours.")
        elif choice3 == "Red" or choice3 == "RED" or choice3 == "red":
            print("OOPS!! The room is full of beasts. you die.. Game Over..")
        else:
            print("Hey.. Someone has locked the room from outside.. And whats that smell?? Shitt!! This room is burning.. Game Over")
    else:
        print("You became a tasty dinner for the crocodiles. Game Over")
else:
    print("I told you.. It was a mysterious Island.. It was full of Dragons.. Now you are inside the belly of a dragon. Game Over")