_userInput = input("What excersise do you want to run?: ")
match _userInput:
    case "1":
        _userInput = input("Do you have a ticket? Y/N: ").capitalize()
        if(_userInput == "Y"):
            print("You may enter")
        else:
            print("You cannot enter")
    case "2":
        _userAge = int(input("What is your age?: "))
        _userID = input("Do you have ID? Y/N: ").capitalize()
        if(_userInput == "Y" and _userAge >= 18):
            print("You may enter")
        else:
            print("You cannot enter")
    case "3":
        _userInput = input("What is the weather like?\n1 ~ Sunny\n2 ~ Rainy\n3 ~ Other\n")
        if(_userInput == "1"):
            print("Go outside")
        elif (_userInput == "2"):
            print("Bring an Umbrella")
        else:
            print("Do not go out")
            