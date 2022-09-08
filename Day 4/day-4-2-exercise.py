import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
names_lenght = len(names) - 1
pick = random.randint(0, names_lenght)

print(f"{names[pick]} is going to buy the meal today!")