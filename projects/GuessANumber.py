import random
my_random_number = random.randint(1, 10)
print "I am thinking of a number between 1 and 10. Can you guess what number I am thinking of? You have 3 guesses."
question = int(raw_input("Guess a number. "))
guesses = 3

while my_random_number != question:
  if guesses == 1:
    print "You ran out of guesses."
    break
  elif question > my_random_number:
    guesses = guesses - 1
    print "That is too high. Guess Again."
    question = int(raw_input("Guess a number. "))
  elif question < my_random_number:
    guesses = guesses - 1
    print "That is too low. Guess again."
    question = int(raw_input("Guess a number. "))
  elif question == my_random_number:
    print "You win!"
    break


