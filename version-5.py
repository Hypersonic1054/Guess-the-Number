import random as rd

magic_number = rd.randint(1, 100)
print(magic_number)

guess = int(input("Guess a number between 1 and 100: "))
counter = 4
Guess_list = [guess]


while guess != magic_number and counter > 0:
  if guess > magic_number:
    print("too high")
  elif guess < magic_number:
    print("too low")
  print("Try again!")
  print("%s guesses remain." %(counter))
  guess = int(input("Guess a number between 1 and 100: "))
  counter-= 1
  Guess_list.append(guess)
  print ("You have already guessed :%s" %Guess_list)
  print ("over")
else:
  print ("under")

  
if counter == 0:
  print ("You lose!")
else: 
  print("You win!")

