#Calculator in Python
import math
operator = input("Enter an operator(): ")
def chosen_operator(operator):
    match operator:
        case "root":
            num1 = int(input("Enter a number: "))
            return math.sqrt(num1)
        case "square":
            num1 = int(input("Enter a number: "))
            return pow(num1, 2)
        case "pi":
            return math.pi
        case "sin":
            num1 = int(input("Enter a number: "))
            return math.sin(math.radians(num1))
        case "cos":
            num1 = int(input("Enter a number: "))
            return math.cos(math.radians(num1))
        case "tan":
            num1 = int(input("Enter a number: "))
            return math.tan(math.radians(num1))
        case "+":
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            return num1 + num2
        case "-":
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            return num1 - num2
        case "*":
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            return num1 * num2
        case "/":
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            while True:
                if num2 == 0:
                    print("You cannot divide by zero")
                    num2 = int(input("Enter another number: "))
                return num1 / num2
print(chosen_operator(operator))