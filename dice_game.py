import random

def roll_dice():
  return random.randint(1,6)+random.randint(1,6)
def main():
  player1=input("enter player 1's name:\n")
  player2=input("enter player 2's name:\n")

  roll1=roll_dice()
  roll2=roll_dice()

  print(player1,"rolled a", roll1)
  print(player2, "rolled a", roll2)
  if roll1>roll2:
    print(player1, "wins")
  elif roll2>roll1:
    print(player2, "wins")
  else:
    print("it's a tie!")
main()