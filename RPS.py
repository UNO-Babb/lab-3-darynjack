#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  playAgain = "Y"
  while playAgain == "Y": #Determine winner and state what happened to the user
    computer = random.choice( ["R", "P", "S"] )
    player = input("Pick your weapon (R, P, S): ")

    if computer == "R": 
      print("Computer chose Rock")
    elif computer == "P":
      print("Computer chose Paper")
    else:
      print("Computer chose Scissors") 

    if player == "R": 
      print("Player chose Rock")
    elif player == "P":
      print("Player chose Paper")
    else:
      print("Player chose Scissors") 

    if player == "R" and computer == "R":
      print("Tie")
      ties = ties + 1
    if player == "R" and computer == "P":
      print("Computer Wins")
      losses = losses + 1
    if player == "R" and computer == "S":
      print("You win!")
      wins = wins + 1
    if player == "P" and computer == "P":
      print("Tie")
      ties = ties + 1
    if player == "P" and computer == "R":
      print ("Win")
      wins = wins + 1
    if player == "P" and computer == "S":
      print("loss")
      losess = losses + 1
    if player == "S" and computer == "S":
      print("tie")
      ties = ties + 1
    if player == "S" and computer == "R":
      print("loss")
      losses = losses + 1
    if player == "S" and computer == "P":
      print("win")
      wins = wins + 1
  #Ask the user if they would like to play again.
    playAgain = input("Play again? (Y/N): ")
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
