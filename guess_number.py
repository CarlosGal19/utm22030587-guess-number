print("\n***FIND THE NUMBER***\n")
print("Instructions. You have to select a range, a number is going to be selected and you have to find the number before running out of points or you will lose.\n")

from random import randint



minNumber = int(input("Write the miminum value of the range: "))
maxNumber = int(input("Write the maximum value of the range: "))
randomNumber = randint(minNumber, maxNumber)
print("\nThe number has been selected.\n")

puntos=100
i=1
num=randomNumber+1
while num!=randomNumber:		
	if puntos > 0:
		num = int(input("Attempt {}, enter a number: ".format(i)))
		if num > randomNumber:
			print("\nThe number is less\n")
			puntos=puntos-10
			print("Points: ",puntos)
			i=i+1
		elif num<randomNumber:
			print("\nThe number is greater\n")
			puntos=puntos-10
			print("Points: ",puntos,"\n")
			i=i+1
		else:
			print("\nYOU HAVE WON IN",i,"ATTEMPTS.\n")
			print("Final points: ",puntos,"\n")	
	else:
		print("\nYou lost, the number was: ",randomNumber,"\n")
		num=randomNumber

