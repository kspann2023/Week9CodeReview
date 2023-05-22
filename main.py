# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Kayla Ledger
# Creation Date: 5/14/2023
# Below is a simple program with several.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
  #There is an indentation Error. To fix this we need to move the indentation to the appropriate spot in the code. 
    while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
            cave = input()
#When running the code there was a name defined error. To fix this the name needed to be changed to cave because that is the defined name, not caves.
    return cave

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
    #There is a syntax error on this line. There is missing parentheses in the print. To fix this there will be () added to the print statement. 
      print ('Gobbles you down in one bite!')


displayIntro()
#There is a NameError. choosecave is not defined. To fix this the c in cave needs to be capitalized to be chooseCave since that is the defined name.
caveNumber = chooseCave()
checkCave(caveNumber)
#There is a typo in the print. It should be playing instead of planing. 
print("Thanks for playing")