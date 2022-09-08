import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(choose)
if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)
else:
    print("Choose correct value.")


ai_choose = random.randint(0,2)

print(ai_choose)
if ai_choose == 0:
    print(rock)
elif ai_choose == 1:
    print(paper)
elif ai_choose == 2:
    print(scissors)
    
if choose == ai_choose:
    print("It's a draw.")
elif choose == 0 and ai_choose == 2:
    print("You win.")
elif choose == 2 and ai_choose == 0:
    print("You lose.")
elif choose == 1 and ai_choose == 0:
    print("You win.")
elif choose == 0 and ai_choose == 1:
    print("You lose.")
elif choose == 1 and ai_choose == 2:
    print("You lose.")
elif choose == 2 and ai_choose == 1:
    print("You win.")
