import getpass

print("\n***GUESS THE NUMBER MULTIPLAYER***\n")
print("Instructions. Player 1 has to enter a number, and player 2 has to guess the number before he/she ran out of points.\n")

hidNumber = getpass.getpass("(Player 1) Write the number to be guessed: ")
hidNumber = int(hidNumber)

p2Points = 100
i=1
guess=hidNumber+1

while guess!=hidNumber: 
        if p2Points>0:
            guess = int(input("(Player 2) Attempt {}. Guess the number\n".format(i)))

            if guess>hidNumber:
                     print("\nThe number must be less\n")
                     p2Points=p2Points-10
                     print("Your current score is: ", p2Points)
                     i=i+1
            elif guess<hidNumber:
                     print("\nThe number must be greater\n")
                     p2Points=p2Points-10
                     print("Your current score is: ", p2Points)
                     i=i+1


            else:
                     print("\n(Player 2) You won with ", i, "attempts\n" "Your final score is: ", p2Points)
        else:
              print("Player 1 wins, the number was :", hidNumber)

            
