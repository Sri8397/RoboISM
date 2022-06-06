def Calculator(firstNumber, operator, secondNumber): 
    if operator == '+':
        return firstNumber + secondNumber
    elif operator == '-':
        return firstNumber - secondNumber
    elif operator == '*':
        return firstNumber * secondNumber
    else: 
        if secondNumber == 0:
            return "Can't divide by 0"
        else: 
            return firstNumber / secondNumber

firstNumber = int(input("Enter the first number: "))
operator = input("Enter operator(+, -, * or /): ")
secondOperator = int(input("Enter the second number: "))
print(Calculator(firstNumber, operator, secondOperator))