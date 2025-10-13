"""
•	Keep the game within the 1..100 range.
•	Add sensible input validation (e.g., non-numeric or out-of-range values).
•	BONUS (optional):
•	Count and display the number of attempts.
•	Offer to play again without restarting the programme.
•	Add a max attempts mode (e.g., 10 tries). 
"""

import random

while True:
    _randomNumber = random.randint(0, 100)
    _userInput = input("Please enter a number between 0 and 100, inclusive: ")
    i = 0
    while _userInput != _randomNumber and i <= 4:
        while True:
            try:
                _userInput = int(_userInput)
            except:
                print("Please make certain your input is an integer.")
                _userInput = input("Please enter a number between 0 and 100, inclusive: ")
                continue

            if (_userInput < 0 or _userInput > 100):
                    print("Please make certain your input is between 0 and 100, inclusive.")
                    _userInput = input("Please enter a number between 0 and 100, inclusive: ")
                    continue
            else:
                break
        print("Not Quite!")
        i+=1
        if (i <= 4):
            _userInput = input("Please enter a number between 0 and 100, inclusive: ")

    #_randomNumber = random.randint(0, 100)
    if(_userInput == _randomNumber):
        print("\nYou guessed " + str(_userInput) + ", the correct answer was " + str(_randomNumber) + ". Congrats!")
    else:
        print("\nYou guessed " + str(_userInput) + ", the correct answer was " + str(_randomNumber) + ". Better luck next time!")
    
    if(input("\nWould you like to play again? Y/N ") == "Y"):
        continue
    else:
        break