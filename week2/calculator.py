while True:
    print("\nMy simple calculator")
    print("-----------------------\n")
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a second number: "))
    op = input("Enter an operator (+, -, * or /): ")
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        break
