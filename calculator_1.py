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

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero.")
    return a % b

def show_history(history):
    if not history:
        print("\nNo calculations yet.")
    else:
        print("\n--- Calculation History ---")
        for i, entry in enumerate(history, 1):
            print(f"  {i}. {entry}")
        print("---------------------------")

def calculator():
    print("Simple Calculator")
    print("-----------------")
    print("Operations: +  -  *  /  **  %")
    print("Type 'history' to view past calculations, 'clear' to clear history, or 'quit' to exit.")

    history = []

    while True:
        try:
            user_input = input("\nEnter first number (or 'history' / 'clear' / 'quit'): ").strip().lower()

            if user_input == "quit":
                print("Goodbye!")
                break
            elif user_input == "history":
                show_history(history)
                continue
            elif user_input == "clear":
                history.clear()
                print("History cleared.")
                continue

            a = float(user_input)
            op = input("Enter operator (+, -, *, /, **, %): ").strip()
            b = float(input("Enter second number: "))

            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            elif op == "**":
                result = power(a, b)
            elif op == "%":
                result = modulo(a, b)
            else:
                print("Invalid operator. Please use +, -, *, /, **, or %.")
                continue

            expression = f"{a} {op} {b} = {result}"
            print(f"Result: {expression}")
            history.append(expression)

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
