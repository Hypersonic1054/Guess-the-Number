import random as rd

magic_number = rd.randint(1, 10)
#3print(magic_number)

guess = int(input("Guess a number between 1 and 10: "))
counter = 2

while guess != magic_number and counter > 0:
  print("Try again!")
  guess = int(input("Guess a number between 1 and 10: "))
  counter-= 1

if counter == 0:
  print ("You lose!")
else: 
  print("You win!")

  
  
  
  
