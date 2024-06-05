# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:21:31 2024

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

def perform_operation(choice, num1, num2):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        return num1 / num2 if num2 != 0 else "undefined (division by zero)"
    elif choice == 5:
        return num1 // num2 if num2 != 0 else "undefined (division by zero)"
    elif choice == 6:
        return num1 % num2 if num2 != 0 else "undefined (division by zero)"
    elif choice == 7:
        return num1 ** num2

def is_even_or_odd(number):
    if isinstance(number, (int, float)):  # Check if the number is numeric
        if number % 2 == 0:
            return "even"
        else:
            return "odd"
    else:
        return "undefined"  # For non-numeric results (like division by zero)

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
            print("Thank you for using Kaylne's calculator.Ciao!")
