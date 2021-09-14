import random
def rolls():
  computer_roll=random.randint(1,100)
  name=input("what's your name?\n")
  tries=1
  guess_roll=int(input('guess the dice roll:\n'))
  while computer_roll!=guess_roll:
    if computer_roll>guess_roll:
      print("you guessed too low, try again")
      tries+=1
      guess_roll=int(input('guess the dice roll:\n'))
    elif computer_roll<guess_roll:
      print("you guessed too high, try again")
      tries+=1
      guess_roll=int(input('guess the dice roll:\n'))
  if computer_roll == guess_roll:
    print("Well done "+name+"! You found my number in "+str(tries)+" tries!")

rolls()