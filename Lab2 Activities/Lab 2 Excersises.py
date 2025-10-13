_userInput = input("What excerise to run?")
match _userInput:
    
    case "1":
        itemPrice = float(input("Enter the item price: ")) 
        itemTax = itemPrice * 0.2
        totalPrice = itemPrice + itemTax
        print("Tax on the item is", itemTax)
        print("Total item price is", totalPrice)
        _quantityToPurchase = int(input("How many items do you wish to buy?")) #Takes input for how many to purchase and casts to int
        _priceForProducts = totalPrice * _quantityToPurchase
        print(f"The price for the items is {round(_priceForProducts,2)}") #Limits total cost to 2dp (For currency) and prints
    
    case "2":
        year = int(input("Enter the year you were born: "))
        if year % 4 == 0:
            print("You were born in a leap year")
        else:
            print("You were not born in a leap year!")
        
        if year > 2007:
            print("You are younger than me!")
        elif year < 2007:
            print("You are older than me!")
        else:
            print("You were born in the same year as me!")
    
    case "3":
        half = 1.0/2.0
        print(type(half))
        print(f"One half (1/2) = {half}")
    
    case "4":
        _userInput = int(input("What is the temperature in C? "))
        _tempInF = _userInput * (9/5) + 32
        print(f"{_userInput}C in F is {_tempInF}F")
    
    case "5":
        _conversionRate = float(input("£1 in $ is: "))
        _userInput = input("Which do you wish to do?\n1 ~ Convert £ to $\n2 ~ Convert $ to £")
        match _userInput:
            case "1":
                _userInput = float(input("Enter the amount in £ to convert"))
                _convertedSum = _userInput * _conversionRate
                print(f"The converted value of £{_userInput} is ${round(_convertedSum,2)}")
            case "2":
                _userInput = float(input("Enter the amount in $ to convert"))
                _convertedSum = _userInput / _conversionRate
                print(f"The converted value of ${_userInput} is £{round(_convertedSum,2)}")

    case "6":
        _userInput = input("Please enter 5 numbers, seperated by ,")
        _listNumbers = _userInput.split(",")
        _listNumbers.sort()
        _listNumbers.reverse()
        print(f"The largest number entered was {_listNumbers[0]}")
    
    case "7":
        _userInput = input("Please enter a list of numbers, seperated by ,\n")
        _listNumbers = _userInput.split(",")
        #sorted = False
        i = 0
        swapped = False
        while(True):
            #Compare current number with adjacent number
            if (i + 1 < len(_listNumbers)):
                _currentNumber = int(_listNumbers[i])
                _nextNumber = int(_listNumbers[i + 1])
                if _currentNumber > _nextNumber:
                    _listNumbers[i] = _nextNumber
                    _listNumbers[i+1] = _currentNumber
                    swapped = True
                i = i + 1
            elif (i + 1 == len(_listNumbers)):
                i = 0
                if(swapped == False):
                    break
                    #sorted = True
                else:
                    swapped = False
                
        
        print (f"In ascending order, the list is {_listNumbers}")