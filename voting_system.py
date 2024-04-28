""" AUTHOR  - PRINCE SHARMA
    DATE    - 28/4/2024 4:06 PM
    WORKING - VOTING SYSTEM
"""

members = ["AAP", "BSP", "BJP", "CPI", "INC", "NPP"]

try :
    age = int(input("Enter Your Age - "))
            
    if age <= 0 :
        raise ValueError
    elif age < 18 :
        print("You Are Not Able To Vote")
        quit()
        
    for number in range(1, len(members) + 1) :
        print(number, members[number - 1])
        
    vote = int(input("Enter Your Vote - "))
            
    if vote <= 0 or vote > len(members) :
        raise ValueError

    print("You voted", members[vote - 1])
except :
    print("Invalid Input")