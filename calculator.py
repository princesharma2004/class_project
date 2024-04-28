""" AUTHOR  - PRINCE SHARMA
    DATE    - 23/4/2024 5:42 PM
    WORKING - CALCULATOR
"""

from math import *

try :
    equation = input("Enter Equation - ")
    result = round(eval(equation), 2)
    print(equation, "=", result)    
except ZeroDivisionError :
    print("Not Defined")
except (NameError, TypeError) :
    print("Invalid Input")