#rock, paper, scissors game
#logic 
import random

choices = ["rock", "paper", "scissors"]
computerChoice = random.randint(1, 3)


playerChoice  = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))
try:
    if playerChoice < 1 or playerChoice > 3:
        raise ValueError("Error: Choice must be between 1 and 3")
except ValueError as e:
    print(e)
    exit(1)

playerChoiceIndex = choices[playerChoice - 1]
computerChoiceIndex = choices[computerChoice - 1]
print(f"You chose: {playerChoiceIndex}")
print(f"Computer chose: {computerChoiceIndex}")

if playerChoice == computerChoice:
    print("It's a tie!")
if playerChoice == 1 and computerChoice == 3:
    print(f"Your choice {playerChoiceIndex} beats computer's choice {computerChoiceIndex}Rock beats Scissors - You win!")
elif playerChoice == 2 and computerChoice == 1:
    print(f"Your choice {playerChoiceIndex} beats computer's choice {computerChoiceIndex}Paper beats Rock - You win!")
elif playerChoice == 3 and computerChoice == 2:
    print(f"Your choice {playerChoiceIndex} beats computer's choice {computerChoiceIndex}Scissors beats Paper - You win!")   
else:
    print("You lose!")