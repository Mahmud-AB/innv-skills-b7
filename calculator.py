#calculator
while True:
    choice = str(input("Enter Sum for addition, Sub for subtraction, Mul for multiplication, Div for division, e for exit: "))
    if choice in ['Sum','Sub','Mul','Div']:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == 'Sum':
            print(f"Sum of {num1} and {num2} is {num1+num2}")
        elif choice == 'Sub':
            print(f"Subtraction of {num1} and {num2} is {num1-num2}")
        elif choice == 'Mul':
            print(f"Multiplication of {num1} and {num2} is {num1*num2}")
        elif choice == 'Div':
            print(f"Division of {num1} and {num2} is {num1/num2}")
    elif choice == 'e':
        break
    else:
        print("Invalid choice")