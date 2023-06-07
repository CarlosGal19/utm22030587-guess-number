import getpass      #Se importa libreria para ocultar el numero a adivinar

print("\n***GUESS THE NUMBER MULTIPLAYER***\n")                                                                #Se imprime el titulo del juego y las instrucciones para jugar
print("Instructions. Player 1 has to enter a number, and player 2 has to guess the number before he/she ran out of points.\n")

hidNumber = getpass.getpass("(Player 1) Write the number to be guessed: ")      #Se define el numero a adivinar
hidNumber = int(hidNumber)

p2Points = 100                                  #Se definen los puntos del jugador 2, el contador y una variable distinta al numero oculto para iniciar el juego
i=1                                                
guess=hidNumber+1

while guess!=hidNumber:                         #Mientras que la variable guess sea diferente a de el numero oculto
        if p2Points>0:                              #Si los puntos del jugador 2 son mayores a 0
            guess = int(input("(Player 2) Attempt {}. Guess the number\n".format(i)))               #Se le da un nuevo valor a la variable guess

            if guess>hidNumber:                                                     #Si la variable guess es mayor al numero oculto
                     print("\nThe number must be less\n")                           #Se indica que el numero debe ser menor
                     p2Points=p2Points-10                                           #Se restan 10 puntos al puntaje del jugador 2
                     print("Your current score is: ", p2Points)                     #Se muestra la puntuacion actual del jugador 2
                     i=i+1                                                          #Se aumenta el contador
                                                         
            elif guess<hidNumber:                                                   #Si la variable guess es menor que el numero oculto
                     print("\nThe number must be greater\n")                        #Se indica que el numero debe ser menor
                     p2Points=p2Points-10                                           #Se restan 10 puntos al puntaje del jugador 2
                     print("Your current score is: ", p2Points)                     #Se muestra la puntuacion actual del jugador 2
                     i=i+1                                                          #Se aumenta el contador


            else:                                                                   #Si no, se imprime un mensaje que indica que el jugador 2 ganó
                     print("\n(Player 2) You won with ", i, "attempts\n" "Your final score is: ", p2Points)
        else:                                                                       #Si no, se imprime un mensaje que indica que el jugador 1 ganó
              print("Player 1 wins, the number was :", hidNumber)

            
