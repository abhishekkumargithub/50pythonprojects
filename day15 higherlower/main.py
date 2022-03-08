from art import logo
from game_data import data
from art import vs
import random


def format_data(account):
  """fromat the data into a prinatble format"""
  account_name=account["name"]
  account_desc=account["description"]
  account_country=account["country"]
  return f"{account_name}, a {account_desc},from {account_country}"

def check_answer(guess,a_followers,b_followers):
  '''Take the users guess and follwer counts and return if they got it right.'''
  if a_followers>b_followers:
    return guess=="a"
  else:
    return guess=="b"
#display art
print(logo)
score=0
game_should_continue=True

#making account at position B becomes the next account at position A
account_b =random.choice(data)

#make the game repeatable 
while game_should_continue:
  #genertre random account from the data
  account_a =account_b
  account_b=random.choice(data)
  while account_a ==account_b:
    account_b=random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Compare B: {format_data(account_b)}.")

  #ask the user for guess
  guess= input("Who has more followers? Type'A' or 'B': ").lower()

  #check if the user is correct
  #get follwer count on each object
  a_followers_count=account_a["follower_count"]
  b_followers_count=account_b["follower_count"]
  is_correct=check_answer(guess,a_followers_count,b_followers_count)
  
  #clear the screen between rounds
 
  print(logo)

  #use if statment if the user is correct
  if is_correct:
    score+=1
    print(f"You're right!!, current_score ={score}")
  else:
    game_should_continue=False
    print(f"You're wrong!!, current_score={score}")



