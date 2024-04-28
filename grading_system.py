""" AUTHOR  - PRINCE SHARMA
    DATE    - 28/4/2024 4:06 PM
    WORKING - GRADING SYSTEM
"""

grades = ["O", "A+", "A", "B+", "B", "C", "P"]

try :
    percentage = round(float(input("Enter Your Percentage (0-100)- ")), 2)
    
    if percentage < 0 or percentage > 100 :
        raise ValueError
    
    if percentage > 39 :
        print(grades[9 - int((percentage - 1)//10)])
    else :
        print("F")   
except :
    print("Invalid Input")