from art import logo
def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n12
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
     return n1 / n2
calc_operations ={
  "+" : add,
  "-" : subtract,
  "*" :multiply,
  "/" :divide
 
}
def calculator():
  print(logo)
  num1 = float(input("Enter the first number:"))
  for oper in calc_operations:
    print(oper)
  should_continue=True
  while should_continue:
    choice=input("Pick an operation from the line above: \n")
    num2 = float(input("Enter the next number:"))
    calc_func = calc_operations[choice]
    answer = calc_func(num1,num2)
    print(f"{num1}{choice}{num2}={answer}")
    if input(f"Type 'y' to continue calculating with {answer},or type 'n' to exit:")=='y':
      num1=answer
    else:
      should_continue=False
      calculator()
calculator()
  