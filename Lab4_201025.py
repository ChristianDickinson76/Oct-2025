import math


_userInput = int(input("What task to run? "))
match _userInput:
    case 1:
        _attempts = 3
        password = "password123"
        for _attempts in range(3,0,-1):
            _userInput = input("Please enter password:\n")
            if _userInput == password:
                print("You have gained access to the system")
                break
            elif _userInput != password and _attempts == 1:
                print("You are out of attempts, please contact a system administator")
                break
            else:
                print("Incorrect, {_attempts}")
                continue
        quit()
    case 2:
        
        for i in range(1,11):
            print("")
            for i in range(1,21):
                print("x", end="")
        print("")
        
        for i in range(1,11):
            print("")
            for i in range(1,6):
                print("x", end="")
        print("")
        
        for i in range(1,12):
            print("")
            for i in range(1,5):
                print("x", end="")
        for i in range(1,5):
            print("")
            for i in range(1,21):
                print("x", end="")
        print("")

        for i in range(1,6):
            print("")
            for i in range(1,21):
                print("x", end="")
        for i in range(1,6):
            print("")
            print("     ", end = "")
            for i in range(1,11):
                print("x", end="")

        quit()

    case 3:
        num = 0
        for i in range(1,6):
            print("")
            for f in range(1,8):
                print(f"{i+f:02}", end=" ")
    
    case 4:
        _userInput = int(input("Please enter a year: "))
        _monthDays = [
            ["January", 31],
            ["February", 28],  # 29 in leap years
            ["March", 31],
            ["April", 30],
            ["May", 31],
            ["June", 30],
            ["July", 31],
            ["August", 31],
            ["September", 30],
            ["October", 31],
            ["November", 30],
            ["December", 31]
        ]
        
        if(_userInput % 4 == 0 and (_userInput % 100 != 0 or _userInput % 400 == 0)):
            _monthDays[1][1] = 29
        for i in range (1, 13):
            day = 0
            print(f"\n{_monthDays[i-1][0]}")
            print("Mon Tue Wed Thu Fri Sat Sun")
            for j in range (0, math.ceil(_monthDays[i-1][1] / 7)):
                for k in range (0, 7):
                    if(j*7+(k+1) <= _monthDays[i-1][1]):
                        print(f"{j * 7 + (k+1):03}", end = " ")
                    else:
                        print("   ", end = " ")
                print("")