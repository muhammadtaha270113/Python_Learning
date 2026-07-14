def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Error! Division by zero is not allowed.")
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def main():
    print("=== Python Calculator ===")
    
    while True:
        print("\nSelect an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
            
        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please select a valid option (1-5).")
            continue
            
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        if choice == '1':
            result = add(num1, num2)
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == '4':
            try:
                result = divide(num1, num2)
                print(f"\nResult: {num1} / {num2} = {result}")
            except ValueError as e:
                print(f"\n{e}")
                
        # Ask if the user wants to perform another calculation
        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again not in ('y', 'yes'):
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
