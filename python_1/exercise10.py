#The computer guesses your number

low = 1
high = 100
guesses = 0

print("Think of a number from 1 to 100.")

while low <= high:
    guess = (low + high) // 2
    answer = input("Is it " + str(guess) + "? (h/l/c) ")
    guesses += 1

    if answer == "c":
        print("Found it in", guesses, "guesses!")
        break
    elif answer == "h":
        low = guess + 1
    elif answer == "l":
        high = guess - 1
