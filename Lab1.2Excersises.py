def converter(userinput, convtype):
    if convtype == 'dec-bin':
        print(("Binary:  " + bin(int(userinput))[2:]))
        return bin(ord(userinput))[2:]
    elif convtype == 'dec-hex':
        print(("Hex: " + hex(int(userinput))[2:]))
        return hex(ord(userinput))[2:]
    elif convtype == 'hex-dec':
        print(("Dec: " + str(int(userinput, 16))))
        return int(userinput, 16)
    elif convtype == 'bin-dec':
        print("Decimal: " + str(int(userinput, 2)))
        return int(userinput,2)
    else:
        print(("Binary:  " + bin(int(userinput))[2:]))
        print(("Hex: " + hex(int(userinput))[2:]))
        return None


_userInput = input("Please select a program (Con or Calc): ")
if _userInput == "Con":
    _userInput = input("Please input a character: ")
    converter(_userInput, "")

else:
    _userInput = input("Please input a character: ")
    convtype = input ("Please input the type of conversion: ")
    _firstNo = converter(_userInput, convtype)

    _userInput = input("Please input a character: ")
    convtype = input("Please input the type of conversion: ")
    _secondNo = converter(_userInput, convtype)

    oper = input("Choose a math operation (+, -, *, /): ")
    if oper == "+":
        print(_firstNo + _secondNo)
    elif oper == "-":
        print(_firstNo - _secondNo)
    elif oper == "*":
        print(_firstNo * _secondNo)
    else:
        print(_firstNo / _secondNo)