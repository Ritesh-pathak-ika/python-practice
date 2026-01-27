import random
print("Guess Game")
print("*******")

Guess = random.randint(1,10)
attempts=choose=0

while choose != Guess:
    choose=int(input("Enter your number:"))
    attempts += 1
    
    if choose > Guess:
        print("This number is too High")

    elif choose < Guess:
        print("This number is too Low")

    else:
        print("Correct Answer")











  