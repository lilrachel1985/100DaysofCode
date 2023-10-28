from random import randrange
from game_data import data

A = randrange(len(data))
item1=dict(data[A])

  
print(f"Compare A: {item1['name']} , a {item1['description']} from {item1['country']}")

B = randrange(len(data))
item2=data[B]
print(f"Against B:{item2['name']}, a {item2['description']} from {item2['country']}")

game_completed=False
user_choice=input("Who has more followers. Type 'A' or 'B':")

def is_greater(first,second):
   if item1['follower_count']> item2['follower_count']:
     return item1['name']
   else:
     return item2['name']
is_greater(first=item1,second=item2)
  
  
   