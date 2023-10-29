from random import randrange
from game_data import data

from art import logo
def check_answer(guess,item1,item2):
  if item1['follower_count']>item2['follower_count']:
    if guess=="a":
       return A
  else:
    if guess=="b":
      return B
score=0
game_should_continue=True
B=randrange(len(data))
item2=dict(data[B])
while game_should_continue:
 
  A = randrange(len(data))
  item1=dict(data[A])
  print(f"Compare A:{item1['name']} ,a {item1['description']} from {item1['country']}") 
  print(logo)
  B=randrange(len(data))
  item2=dict(data[B])
  print(f"Against B:{item2['name']}, a {item2['description']} from {item2['country']}")
 
  guess=input("Who has more followers. Type 'A'or 'B':").lower()
  
  is_correct=check_answer(guess,item1,item2)
  if is_correct:
    score+=1
    print(f"You're right! Current score:{score}")
  else:
    print(f"You're wrong! Final score: {score} ")
 

      
      
        
           
 


  
  