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