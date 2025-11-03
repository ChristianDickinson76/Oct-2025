# Task 1: Calculate CDF for a Fair Die Roll 
# Task 2: Calculate PMF for a Fair Die Roll
# Task 3: Create a Stem Plot for Exam Scores 
# Task 4: Plot CDF for a Normal Distribution 
# Task 5: Calculate CDF at 170 cm for a Normal Distribution 
# Task 6: Calculate PDF at 170 cm for a Normal Distribution 
# Task 7: Calculate CDF Using Z-Score

_userInput = int(input("Please select a task"))
match _userInput:
    case 1:
        print("1")
    case 2:
        print("1/6")
    case 3:
        _userInput = input("Please input a list of numbers to add to a stem and leaf diagram: ")
        
        _numberArray = _userInput.split(",")
        _largestNum = 0
        for num in _numberArray:
            if(int(num[0]) > _largestNum):
                _largestNum = int(num[0])
        
        for i in range(1, _largestNum + 1):
            print(f"{i}  ", end = "")
            for num in _numberArray:
                if(int(num[0]) == i):
                    print(f"{int(num[1])} ", end = "")
            print("")   