# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

import random
game_image = [rock, paper, scissors]

you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors  "))

if you>=3 and user<0:
  print("You typed an invalid number, you lose")
else:
  print(game_image[you])

  computer = random.randint(0, 2)
print("Computer chose ")
print(game_image[computer])

if you==0 and computer == 2:
  print("You win!")
elif you==2 and computer == 0:
  print("You lose!")
elif you==computer:
  print("It's a draw")
elif you>computer:
  print("You lose!")
elif you<computer:
  print("You win!")
elif you==2 and computer == 0:
  print("You lose!")
