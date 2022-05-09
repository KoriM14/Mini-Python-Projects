#Number Guessing Game Objectives:

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#check users guess against the answer
def check_answer(guess, answer, turns):
  """checks answer against guess returns number of turns remaining"""
  if guess > answer:
    print("Too High!") 
    return turns -1
  elif guess < answer:
    print("Too Low!")
    return turns -1
  else:
    print(f"You got the answer right! {answer}")

#make difficulty function 
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return  EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
  #choose random number
  print("Welcome to guess my number!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)

  turns = set_difficulty()
 

  #repeat guessing if answer is wrong
  guess = 0 
  while guess != answer:
    print(f"You have {turns} attempts remaining")


    guess = int(input("Make a guess: "))
    
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You have ran out of guesses, you lose!")
      return 
    elif guess != answer:
      print("Guess again")
 
  
game()
