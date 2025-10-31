import random as rd

magic_number = rd.randint(1, 10)
#3print(magic_number)

guess = int(input("Guess a number between 1 and 10: "))
counter = 2
Guess_list = [guess]


while guess != magic_number and counter > 0:
  print("Try again!")
  print("%s guesses remain." %(counter))
  guess = int(input("Guess a number between 1 and 10: "))
  counter-= 1
  Guess_list.append(guess)
  print ("You have already guessed :%s" %Guess_list)
if counter == 0:
  print ("You lose!")
else: 
  print("You win!")


