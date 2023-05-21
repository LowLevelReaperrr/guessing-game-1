import random

secret_num = random.randint(1, 9)
guesses = 3

run = "Y"


while run == "Y":
    guess = int(input("Enter a number: "))

    if guess < secret_num:
        print("Too low! Try Again!")
    elif guess > secret_num:
        print("Too high! Try Again!")
    elif guess == secret_num:
        print("Exactly Right!")
        run = input("Do you want to continue? (Y/N): ").upper()
    else:
        print("Try Again")









