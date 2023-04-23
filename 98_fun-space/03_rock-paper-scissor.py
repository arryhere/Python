import random

print('Welcome to rock paper scissor game !')
print('Choose your option: rock(-1), paper(0), scissor(1)')
print('You have 10 chances, Good Luck !\n')

choice = {
    -1: 'rock',
    0: 'paper',
    1: 'scissor'
}

computerScore: int = 0
userScore: int = 0

for i in range(0, 10):
  print(f'Round {i+1}')
  while True:
    try:
      user = int(input('Your choice > '))
      if (user == -1 or user == 0 or user == 1):
        break
      else:
        raise ValueError
    except:
      print('Please enter a valid option, rock(-1), paper(0), scissor(1)')

  computer = random.randint(-1, 1)
  print(f"You chose > {choice[user]}\nComputer chose > {choice[computer]}")

  def compare(computerValue: int, userValue: int) -> None:
    global userScore
    global computerScore

    if (computerValue == -1):
      if (userValue == -1):
        print('Tie !\n')
      elif (userValue == 0):
        print('You won !\n')
        userScore += 1
      elif (userValue == 1):
        print('Comouter won !\n')
        computerScore += 1

    elif (computerValue == 0):
      if (userValue == -1):
        print('Comouter won !\n')
        computerScore += 1
      elif (userValue == 0):
        print('Tie !\n')
      elif (userValue == 1):
        print('You won !\n')
        userScore += 1

    elif (computerValue == 1):
      if (userValue == -1):
        print('You won !\n')
        userScore += 1
      elif (userValue == 0):
        print('Comouter won !\n')
        computerScore += 1
      elif (userValue == 1):
        print('Tie !\n')

  compare(computerValue=computer, userValue=user)


print(f"Your total score > {userScore}\nComputer's total score > {computerScore}\n")


if (computerScore > userScore):
  print('You lost !, try again next time')
elif (computerScore == userScore):
  print("It's a tie, try again next time")
elif (computerScore < userScore):
  print('Yon won !, play again')