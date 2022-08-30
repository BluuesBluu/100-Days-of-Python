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

while True:
    crossroad = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\": ")
    lower_crossroad = crossroad.lower()
    
    if lower_crossroad == "left":
        lake = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.: ")
        lowercase_lake = lake.lower()
        break
    elif lower_crossroad == "right":
        print("You fell into a hole. Game Over.")
        print('''
     _.--""--._
    /  _    _  \\
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_\\
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_}
              ''')
        exit()
    else:
        print("Insert correct answer.")
        continue
            
while True:
    if lowercase_lake == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?: ")
        lowercase_door = door.lower()
    elif lowercase_lake == "swim":
        print("You get attacked by an angry trout. Game Over.")
        print('''
     _.--""--._
    /  _    _  \\
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_\\
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_}
              ''')
        exit()
    
    if lowercase_door == "red":
        print("It's a room full of fire. Game Over.")
        print('''
     _.--""--._
    /  _    _  \\
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_\\
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_}
              ''')
        exit()
    elif lowercase_door == "blue":
        print("You enter a room of beasts. Game Over.")
        print('''
     _.--""--._
    /  _    _  \\
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_\\
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_}
              ''')
        exit()
    elif lowercase_door == "yellow":
        print("You found the treasure! You Win!")
        print('''
         __________
        /\____;;___\\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
    ''')
        exit()
    else:
        print("You chose a door that doesn't exist. Try again!")
        continue
    