def problem11(num1, num2):
    try:
        division = num1 / num2
    except ZeroDivisionError:
        division = "Cannot divide by zero."
        
    return division

def problem12(num):
    try:
        result = int(num)
    except ValueError:
        result = "Invalid input. Please enter a number."
    return result

def problem13(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        content = "File not found."
    return content

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Problem 11:", problem11(num1, num2))
num3 = input("Enter a number to divide by 10: ")
print("Problem 12:", problem12(num3))

file_name = input("Enter the file name to read: ")
print("Problem 13:", problem13(file_name))
