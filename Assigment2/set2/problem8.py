from set2.calculator.addition import addition
from set2.calculator.division import division

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
addition_result = addition(num1, num2)
try:
    division_result = division(num1, num2)
except ValueError as e:
    division_result = str(e)
print(addition_result, division_result)