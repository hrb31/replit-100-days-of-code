import os
import time

table = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
global game_over
game_over = 0

def printTable():
  print(table[0] + " |" + table[1] + " |" + table[2])
  print("---------")
  print(table[3] + " |" + table[4] + " |" + table[5])
  print("---------")
  print(table[6] + " |" + table[7] + " |" + table[8])

def checkWin():
  global game_over

  #p1 conditions
  if all(x == "X" for x in [table[0], table[1], table[2]]):
    print("Player 1 wins!")
    game_over = 1
  elif all(x == "X" for x in [table[6], table[7], table[8]]):
    print("Player 1 wins!")
    game_over = 1
  elif all(x == "X" for x in [table[3], table[4], table[5]]):
    print("Player 1 wins!")
    game_over = 1
  elif all(x == "X" for x in [table[0], table[3], table[6]]):
    print("Player 1 wins!")
    game_over = 1
  elif all(x == "X" for x in [table[1], table[4], table[7]]):
    print("Player 1 wins!")
    game_over = 1
  elif all(x == "X" for x in [table[2], table[5], table[8]]):
    print("Player 1 wins!")
    game_over = 1
  elif all(x == "X" for x in [table[0], table[4], table[8]]):
    print("Player 1 wins!")
    game_over = 1
  elif all(x == "X" for x in [table[2], table[4], table[6]]):
    print("Player 1 wins!")
    game_over = 1

  #p2 conditions
  elif all(x == "O" for x in [table[0], table[1], table[2]]):
    print("Player 2 wins!")
    game_over = 1
  elif all(x == "O" for x in [table[6], table[7], table[8]]):
    print("Player 2 wins!")
    game_over = 1
  elif all(x == "O" for x in [table[3], table[4], table[5]]):
    print("Player 2 wins!")
    game_over = 1
  elif all(x == "O" for x in [table[0], table[3], table[6]]):
    print("Player 2 wins!")
    game_over = 1
  elif all(x == "O" for x in [table[1], table[4], table[7]]):
    print("Player 2 wins!")
    game_over = 1
  elif all(x == "O" for x in [table[2], table[5], table[8]]):
    print("Player 2 wins!")
    game_over = 1
  elif all(x == "O" for x in [table[0], table[4], table[8]]):
    print("Player 2 wins!")
    game_over = 1
  elif all(x == "O" for x in [table[2], table[4], table[6]]):
    print("Player 2 wins!")
    game_over = 1

  #draw
  elif " " not in table:
    print("It's a draw!")
    game_over = 1

player1score = 0 
player2score = 0

round = 0 

print("Noughts and Crosses Game\n")
time.sleep(1)
printTable()

while round <10:
  print("Player 1's turn. You are crosses")
  choice1 = int(input("Enter a number from 1 to 9: "))
  if table[choice1 - 1] == " ":
    table[choice1 - 1] = "X"
  else:
    print("That space is taken")
    continue
  printTable()
  checkWin()
  if game_over == 1:
    again = input("Would you like to play again?")
    if again[0].lower() == "y":
      table = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
      os.system('clear')
      print("Noughts and Crosses Game\n")
      printTable()
      game_over = 0
      round = 0
    else:
      print("Thanks for playing!")
      break
  elif game_over == 0:
    round +=1
    os.system('clear')
    print("Noughts and Crosses Game\n")
    time.sleep(1)
    printTable()
    

  print("Player 2's turn. You are noughts")
  choice2 = int(input("Enter a number from 1 to 9: "))
  table[choice2 - 1] = "O"
  printTable()
  checkWin()
  if game_over == 1:
    again = input("Would you like to play again?")
    if again[0].lower() == "y":
      table = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
      os.system('clear')
      print("Noughts and Crosses Game\n")
      printTable()
      game_over = 0
      round = 0
    else:
      print("Thanks for playing!")
      break
  elif game_over == 0:
    round +=1
    os.system('clear')
    print("Noughts and Crosses Game\n")
    time.sleep(1)
    printTable()
    
  
  
    
  
