_userInput = input("Please select an activity to run")
match _userInput:
    case "1":
        for i in range(1,11,1):
            print(f"{i},")
    
    case "2":
        for i in range(1,50,2):
            print(f"{i},")
        print("\n")
        for i in range(100,50,-2):
            print(f"{i},")
    
    case "3":
        _userInput = ""
        while(not (_userInput == "y" or _userInput == "n")):
            _userInput = input("Would you like to delete the record? (y/n) ")
            print(_userInput)
        if(_userInput == "y"):
            print("The record was deleted...")
        else:
            print("The record was not deleted ...")
    
    case "4":
        _userInput = 0
        while(True):
            try:
                _userInput = int(input("Please enter the year you were born: "))
            except:
                print("Please make certain your input is a year between 1900 and 2025")
                continue
            else:
                if(_userInput < 1900 or _userInput > 2025):
                    print("Please check your age is between 1900-2025, inclusive")
                else:
                    break       
        print(f"You are {2025 - _userInput} years old")
    case "5":d
        while (True): 
            while(True):
                try:
                    userNum1 = float(input("Please enter the year you were born: "))
                    break
                except:
                    print("Please make certain your input is a number")
                    continue   
            userNum2 = float(input("Enter second number: ")) #User inputs both numbers for calculations
            userTotal = userNum1 + userNum2 
            print(f"{userNum1} + {userNum2} = {userTotal}") 
            yesNo = input("Do you want another go \033[32m(y/n)\033[0m: ").lower() #input validation
            if (yesNo == 'n'): 
                break #Ends program if n is entered