def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def calculator():
    print("Simple Calculator")
    print("-----------------")
    print("Operations: +  -  *  /")

    while True:
        try:
            a = float(input("\nEnter first number: "))
            op = input("Enter operator (+, -, *, /): ").strip()
            b = float(input("Enter second number: "))

            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print("Invalid operator. Please use +, -, *, or /.")
                continue

            print(f"Result: {a} {op} {b} = {result}")

        except ValueError as e:
            print(f"Error: {e}")

        again = input("\nCalculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()
