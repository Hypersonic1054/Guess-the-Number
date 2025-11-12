import random as rd
import os

play = True
games_played = 0
games_won = 0

while play:
  guess_list = []
  counter = 5
  magic_number = rd.randint(1, 100)
  
  # print(magic_number)
  guess = int(input("Guess a number between 1 and 100: "))
  guess_list.append(guess)
    

  while guess != magic_number and counter > 0:
    counter-= 1
    
    if guess > magic_number:
      print("too high")
    elif guess < magic_number:
      print("too low")
      
    print("Try again!")
    print("%s guesses remain." %(counter))
    print ("You have already guessed :%s" %guess_list)
    guess = int(input("Guess a number between 1 and 100: "))
    guess_list.append(guess)

    
    if counter == 0:
      print ("You lose!")
      games_played += 1
      break
    
  if guess == magic_number:
    print("You win!")
    games_won += 1
    games_played += 1

  print("SCOREBOARD")
  print("----------")
  print("Games Won: %s" % (games_won))
  print("Games Played: %s" % (games_played))      
    
  answer = input("Would you like to play again? (y/n)")
  os.system("clear")
  if answer == "y":
    play = True
  elif answer == "n":
    play = False
