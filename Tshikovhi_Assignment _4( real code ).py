# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:21:29 2024

@author: lk
"""

def print_menu():
    print("Choose an arithmetic operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Normal Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Exponentiation")

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numerical values.")

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def normal_division(num1, num2):
    return num1 / num2 if num2 != 0 else "undefined (division by zero)"

def floor_division(num1, num2):
    return num1 // num2 if num2 != 0 else "undefined (division by zero)"

def modulus(num1, num2):
    return num1 % num2 if num2 != 0 else "undefined (division by zero)"

def exponentiation(num1, num2):
    return num1 ** num2

def perform_operation(choice, num1, num2):
    operations = {
        1: addition,
        2: subtraction,
        3: multiplication,
        4: normal_division,
        5: floor_division,
        6: modulus,
        7: exponentiation
    }
    
    operation = operations.get(choice)
    if operation:
        return operation(num1, num2)
    else:
        return "Invalid operation choice"

def is_even_or_odd(number):
    if isinstance(number, (int, float)):  # Check if the number is numeric
        if number % 2 == 0:
            return "even"
        else:
            return "odd"
    else:
        return "undefined"  
    # For non-numeric results (like division by zero)

def main():
    while True:
        print_menu()
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if choice not in range(1, 8):
                raise ValueError("Invalid choice")
        except ValueError:
            print("Invalid choice. Please choose a valid operation.")
            continue
        
        num1, num2 = get_numbers()
        
        result = perform_operation(choice, num1, num2)
        
        if isinstance(result, str):
            print(f"Result is {result}")
        else:
            print(f"The result of the operation on {num1} and {num2} is {result}")
            print(f"The result is {is_even_or_odd(result)}")
        
        another_operation = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if another_operation != 'yes':
            print("Thank you for using Kaylne's calculator. Ciao!")
            break

if __name__ == "__main__":
    main()
