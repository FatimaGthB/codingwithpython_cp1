import random
n = random.randint (1,100)  # n est le nombre choisi par l'ordinateur
nbr_essais = 5 # nbr_essais est le nombre d'essais qu'a droit l'utilisateur afin
               #  de trouver le correct nombre

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while nbr_essais > 0 :
    nbr_essais -= 1 # le nombre d'essai possible sera réduit de 1 pour chaque entrée de l'utilisateur
    var = int(input("Enter your guess: ")) # var sera le nombre entré par l'utilisateur
    if var > n :
        print("Your guess is too high. Guess again.")
    elif var < n :
        print("Your guess is too low. Guess again.")
    else :
        break
if nbr_essais != 0 :
    print("Congratulations! You guessed the number correctly in " ,5-nbr_essais, "tries !")
else :
    print("sorry the correct number was : ",n)
