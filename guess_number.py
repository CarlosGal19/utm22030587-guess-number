
print("\n***FIND THE NUMBER***\n")
print("Instructions. You have to select a range, a number is going to be selected and you have to find the number before running out of points or you will lose.\n")

from random import randint

minNumber = int(input("Write the miminum value of the range: "))
maxNumber = int(input("Write the maximum value of the range: "))
randomNumber = randint(minNumber, maxNumber)
print("\nThe number has been selected.\n")

	