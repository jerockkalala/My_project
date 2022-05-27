# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Jerock Kalala
# Creation Date: 05-15-2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.
# You need to identify the issues and correct them.

import random
import time

def displayIntro(): # Will suggest lowercase ""display_intro()
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave(): # Will suggest lowercase ""choose_cave()
    cave = '' # Use correct indentation (check for tabs and spaces)
	while cave != '1' and cave != '2': # Use correct indentation (check for tabs and spaces)
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return caves # check the returned variable name. It should be "cave"

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!' # missing parenthesis. It should be print ("Gobbles you down in one bite!")

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y': # equal sign for affectation. "==" should be used
	displayIntro()
	caveNumber = choosecave() # the correct name of the function should be used. It should be "chooseCave()"
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")

