from turtle import clear
from art import logo
from data import data
import random
#clear screen between rounds

#display art


#format account data 4`````6`
def format_data(account):
  """format data in printable form."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return (f"{account_name}, a {account_descr}, from {account_country}")


def check_answer(guess, a_followers, b_followers):
  """use to check if correct. Return correct answer"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


#print logo
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
#repeatable
while game_should_continue:

  # generate random accounts/game data
  # swap account positions

  
  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Against A: {format_data(account_a)}") 
  print ("VS")
  print(f"Against B: {format_data(account_b)}")

  #ask for a guess
  guess = input("Who has more followers? Type 'A or B':").lower()

  #check if user is correct
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  ##use if to check if user is correct
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  clear()
  print(logo)
  #give feedback
  #track score/
  if is_correct:
    score += 1
    print(f"You are right! Current score {score}")
  else:
    game_should_continue = False
    print(f"Sorry that is wrong! Final score {score}")