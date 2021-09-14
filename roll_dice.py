import random
roll=random.randint(1,6)
# print("the computer rolled a "+str(roll))

guess=int(input('guess the dice roll:\n'))
if guess == roll:
  print("correct! They rolled a "+str(roll))
else:
  print("wrong, they rolled a "+str(roll))