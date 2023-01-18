while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        if operation == "+":
            result = num1 + num2
            print("Result:", result)
        elif operation == "-":
            result = num1 - num2
            print("Result:", result)
        elif operation == "*":
            result = num1 * num2
            print("Result:", result)
        elif operation == "/":
            result = num1 / num2
            print("Result:", result)
        else:
            print("Invalid operator. Please enter a valid operator.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a valid number.")
    except:
        print("An error has occurred. Please try again.")