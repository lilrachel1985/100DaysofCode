# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#To concantenate two strings
#combined_name = "name1" + "name2"
#To convert string to a lowercase
lower_name=name1.lower()+name2.lower()
#To count the occurrence of a letter in a string
t=lower_name.count("t")
r=lower_name.count("r")
u=lower_name.count("u")
e=lower_name.count("e")
true=t+r+u+e
l=lower_name.count("l")
o=lower_name.count("o")
v=lower_name.count("v")
e=lower_name.count("e")
love=l+o+v+e
#Adding the two strings
love_total = str(true) + str(love)
#Converting to an integer to be able to do logical comparisons on it

love_score = int(love_total)



if (love_score < 10) or (love_score > 90):
    print(f'Score is {love_score}, you go together like coke and mentos')
elif (love_score >=40 and love_score <=50):
    print(f'Score is {love_score}, you are alright together')
else:
    print(f'Your score is {love_score}')



