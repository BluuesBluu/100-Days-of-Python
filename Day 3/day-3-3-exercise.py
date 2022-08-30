from cgi import test


year = int(input("Which year do you want to check?: "))

test1 = year % 4
test2 = year % 100
test3 = year % 400

if test1 == 0:
    if test2 == 0:
        if test3 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
            
    
    