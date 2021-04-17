from random import randint
t = ["r","s","p"]
computer = t[randint(0,2)]

player = "y"
name = input("enter your name: ")


print("type reset if you want to reset the score: ")
you = 0 
pc = 0



def win():
  global you
  you+=1
  print(message)
  print("computer:",pc,"\n",name,":",you)


def lose():
  global pc
  pc+=1
  print(message)
  print("computer",pc,"\n",name,":",you)

def tie():
  print(message)

while player == "y" or player == "Y":
  player = input("rock,paper or scissor?(r,p,s): ")
  if player==computer:
    print("tie")
  elif player == "r":
    if computer == "p":
      message = "you lose!"
      lose()
    elif player == computer:
      message= "tie"
      tie()
    else:
      message = "you win"
      win()
  elif player == "s":
    if computer == "r":
      message="you lose!"
      lose()
    elif player == computer:
      message= "tie"
      tie()
    
    else:
      message ="you win"
      win()
  elif player == "p":
    if computer == "s":
      message = "you lose!"
      lose()
    elif player == computer:
      message= "tie"
      tie()
    else:
      message = "you win"
      win()
  elif player=="reset":
    you = 0
    pc = 0
    print("score has been reset")
  
  player = input("if you want to continue press y or Y: ")
  computer = t[randint(0,2)]


     

