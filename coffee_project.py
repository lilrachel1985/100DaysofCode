MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def check_resources(coffee_ingredients):
  is_enough = True
  for item in coffee_ingredients:
      if coffee_ingredients[item] >= resources[item]:
          is_enough = False
          print(f"Sorry, there is not enough {item}")
  return is_enough

def process_coins():
   total_coins = 0
   print("Please insert coins")
   quarter_coin = int(input("How many quarters:"))*0.25
   dime_coin = int(input("How many dimes:"))*0.10
   nickel_coin =int(input("How many ncikels:"))*0.05
   penny_coin = int(input("How many pennies:"))*0.01
   total_coins = quarter_coin+dime_coin+nickel_coin+penny_coin
   return total_coins

def transaction_sucessful(money_received,drink_cost):
  """ Return True if payment is accepted else return False
  """
  if money_received > drink_cost:
      change = round(money_received - drink_cost,2)
      print(f" Here is the change {change}$")
      global profit
      profit+=drink_cost
      return change
  else:
      print(f"Sorry, that's not enough money. Refund {money_received}$")
      return money_received

def make_coffee(drink_name,coffee_ingredients):
   """ Deduct the required ingredients from the resources 
   """
   for item in coffee_ingredients:
     resources[item]-=coffee_ingredients[item]
   print(f" Here is your drink {drink_name}") 

profit = 0
completed = False
while not completed:
    prompt = input("What would you like? (espresso/latte/cappuccino):")

    if prompt == "off":
        exit()
    # TODO 3: Print report
    elif prompt == "report":
        print(f"water = {resources['water']}ml")
        print(f"milk = {resources['milk']}ml")
        print(f"coffee = {resources['coffee']}mg")
        print(f"Money = {profit} ")
    else:
       drink = MENU[prompt]
      
       if check_resources(drink['ingredients']):
           payment = process_coins()
           if transaction_sucessful(payment,drink['cost']):
             make_coffee(prompt,drink['ingredients'])