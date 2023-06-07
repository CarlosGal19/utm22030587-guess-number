print("\n***FIND THE NUMBER***\n")
print("Instructions. You have to select a range, a number is going to be selected and you have to find the number before running out of points or you will lose.\n")

from random import randint			# Libreria usada para generar el número random

again="y"							# Variable que usará el ciclo para repetir el juego

while again=="y":					# Ciclo para repetir el juego

	minNumber = int(input("Write the miminum value of the range: "))			# Minimo rango
	maxNumber = int(input("Write the maximum value of the range: "))			# Maximo Rango
	randomNumber = randint(minNumber, maxNumber)								# Numero generado
	print("\nThe number has been selected.\n")

	puntos=100								# Variable para los puntos
	i=1										# Contador de oportunidades
	num=randomNumber+1						# Variable con valor distinto al numero aleatorio para entrar al juego

	while num!=randomNumber:				# Ciclo donde se adivina el numero
		if puntos > 0:						# Si los puntos son mayores a 0 puede jugar, de lo contario habrá perdido
			num = int(input("Attempt {}, enter a number: ".format(i)))		# Intento 'i', ingresa un numero
			if num > randomNumber:											# Si el numero ingresado es mayor, dará una pista y restará 10 puntos
				print("\nThe number is less\n")
				puntos=puntos-10
				print("Points: ",puntos)
				i=i+1
			elif num<randomNumber:											# Si el numero ingresado es menor, dará una pista y restará 10 puntos
				print("\nThe number is greater\n")
				puntos=puntos-10
				print("Points: ",puntos,"\n")
				i=i+1
			else:															# De lo contrario habrá ganado
				print("\nYOU HAVE WON IN",i,"ATTEMPTS.\n")
				print("Final points: ",puntos,"\n")	
		else:
			print("\nYou lost, the number was: ",randomNumber,"\n")			# Al perder muestra el número random
			num=randomNumber												# Num toma el mismo valor que el random para salir del juego

	again=input("Do you want to play again?(y/n): ")						# Pregunta si quiere jugar de nuevo