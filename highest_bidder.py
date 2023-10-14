from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
user_dict={}
bidding_finished = False
def find_high_bidder(bidding_record):
    highest_bidder = 0
    winner=""
    for bidder in bidding_record:
      bid_amount = bidding_record[bidder]
      if bid_amount > highest_bidder:
        highest_bidder =bid_amount
        winner = bidder
    print(f"The winner is {winner} with the highest bid ${highest_bidder}")
        


while not bidding_finished:
  name=input("What is your name? \n")
  amount=int(input("What is your bid price? \n"))
  user_dict[name] = amount
  should_continue = input("Are there any other bidders. Type yes or no \n")   
  if should_continue =='no':
    bidding_finished = True
    find_high_bidder(user_dict)
  elif should_continue =='yes':
    clear()
        
     

  

