""" author - prince sharma
    date   - 14/2/24
    working - rock paper scissor game    
"""

import random

computer=player=0
round=3

print("game rules!\n".title().center(150))
print("1. there are",round,"rounds")
print("2. rock   > scissor and rock   < paper")
print("3. paper  > rock   and paper  < scissor")
print("2. scissor > paper  and sissor < rock")
print()
print("game start!\n".title().center(150))
print()

for i in range(round):
    while True:
        user_choice = input("Enter your choice (rock, paper or scissor): ").lower()
        if user_choice in ['rock', 'paper', 'scissor']:
            break
        else:
            print("Invalid choice. Please try again.")
        
    computer_choice=random.choice(["rock","paper","scissor"])
    
    print("\ncomputer choose :".title(),computer_choice.upper())
        
    if user_choice == computer_choice:
        computer += 1
        player += 1
        print("It's a tie!")
        
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        player +=1
        print("You win!")
        
    else:
        computer += 1
        print("Computer wins!")
        
if player > computer :
    print("player wins!\a".title())
elif player < computer :
    print("computer wins!\a".title())
else :
    print("draw!\a".title())