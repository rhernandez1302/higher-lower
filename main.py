import random
from replit import clear
from game_data import data

from art import logo, vs



points = 0

def gain():
  return points + 1
  
def num_gen():
  rand_choice = (random.randint(0,len(data)-1))
  return rand_choice

points = 0
answers = True
while answers :
  print(logo)
  rand_choice = (random.randint(1,len(data)))
  cp1 = data[num_gen()]
  
  name = (f"Compare A: {cp1['name']}, a {cp1['description']}, from {cp1['country']}.")
  followers = cp1['follower_count']
  print(name)
  print(followers)
  print(vs)
  
  cp2 = data[num_gen()]
  if cp1 == cp2:
    cp2 = data[num_gen()]
  
  name = (f"Compare B: {cp2['name']}, a {cp2['description']}, from {cp2['country']}.")
  followers2 = cp2['follower_count']
  print(name)
  print(followers2)
  
  choice = input("Which one has more followers? Type 'A' or 'B' ")
  
  if choice == 'A':
    choice = followers
    if choice < followers2:
      answers = False
    else:
      points = gain()
      clear()
      print(f"Points: {points}")
  elif choice == 'B':
    choice = followers2
    if choice < followers:
      answers = False
    else:
      points = gain()
      clear()
      print(f"Points: {points}")
    
clear()
print(f"You lose, you managed to get {points} points")
