def quadraticCalc (_xValue, _a, _b, _c):
    return (_a * pow(_xValue, 2) + _b * _xValue + _c)

print(quadraticCalc(1,2,2,2))

def factorial (_value):
    if(_value >= 0):
        outputValue = 1
        for i in range(0, _value - 1, 1):
            outputValue *= _value - i
        return outputValue
    else:
        print("Factorial is undefined for negative numbers")
        return False

print(factorial(-5))

def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

_userInput = input("Please input a word")
if(is_palindrome(_userInput)):
    print(f"{_userInput} is a palindrome")
else:
    print(f"{_userInput} is not a palindrome")
