# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
bmi = weight / height **2
result=round(bmi)
if(result > 0 and result <= 18.5):
    print(f"Your bmi is {result}.You are underweight")
elif(result > 18.5 and result <= 25):
    print(f"Your bmi is {result}. You have a normal weight")
elif(result > 25 and result <= 30):
    print(f"Your bmi is {result}. You are slightly overweight")
elif(result > 30 and result <= 35):
    print(f"Your bmi is {result}. You are obese")
else:
    print(f"Your bmi is {result}. You are clinically obese")
#Write your code below this line 👇
