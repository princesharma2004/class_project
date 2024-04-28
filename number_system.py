""" AUTHOR  - PRINCE SHARMA
    DATE    - 28/4/2024 4:06 PM
    WORKING - NUMBER SYSTEM
"""

try :
    start, end = int(input("Enter starting point - ")) , int(input("Enter End Point - "))
    jump, arrangement = int(input("Enter steps - ")), input("Enter you want (vertical / horizontal) arrangement - ")
    
    if jump < 0 :
        end -= 2
            
    if arrangement.lower() in ["vertical","v"] :
        print_end = "\n"
    elif arrangement.lower() in ["horizontal","h"] :
        print_end = " "
        
    for number in range(start, end + 1, jump) :
        print(number, end = print_end)
except :
    print("Invalid Input")