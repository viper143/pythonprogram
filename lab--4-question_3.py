NUMBER = 10

wrongGuess = True

while wrongGuess:
    number = int(input("Guess a number"))
    if number == NUMBER:
        wrongGuess = False
        print("Well guessed!")
