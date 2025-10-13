_userInput = int(input("Please select an activity to run"))
match _userInput:
    case 1:
        for i in range(1,11,1):
            print(f"{i},")
    
    case 2:
        for i in range(1,50,2):
            print(f"{i},")
        print("\n")
        for i in range(100,50,-2):
            print(f"{i},")
    
    case 3:
        _userInput = ""
        while(not (_userInput == "y" or _userInput == "n")):
            _userInput = input("Would you like to delete the record? (y/n) ")
            print(_userInput)
        if(_userInput == "y"):
            print("The record was deleted...")
        else:
            print("The record was not deleted ...")
        