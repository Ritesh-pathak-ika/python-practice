from random import randint

print("Guess Game")
print("**************\n")

low, high = 1, 50 

secret_number = randint(low, high)
clue = ""

#Game loop

while True:
    guess = input(f"The number is between {low} and {high} {clue}")
    number = int(guess)
    if number > secret_number:
        clue = f"(less than {number})"
    elif number < secret_number:
        clue = f"(greater than {number})"
    else:
        break

print(f"you guessed it! The number is {number}")

