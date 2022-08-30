from turtle import st


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
lower_case_combined = combined_name.lower()

score1 = 0
score2 = 0


true_total= lower_case_combined.count("t") + lower_case_combined.count("r") + lower_case_combined.count("u") + lower_case_combined.count("e")
love_total= lower_case_combined.count("l") + lower_case_combined.count("o") + lower_case_combined.count("v") + lower_case_combined.count("e")

total_score = str(true_total) + str(love_total)

total_score = int(total_score)

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")