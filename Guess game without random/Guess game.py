print("***************Guess the Game***************")
print("Hint:The number is between 2 and 4..")

Guess=int(input("Guess the number:"))

while Guess != 3:
    print(Guess)
    Guess=int(input("Guess the number:"))



print("Congratulations! Your Guess is Correct.")