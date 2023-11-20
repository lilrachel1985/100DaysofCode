import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions=[0,90,180,360]

tim.pensize(5)    
for i in range(500):
    
    tim.seth(random.choice(directions))
    tim.forward(10)
    tim.speed("fastest")
    tim.color(random.choice(colours))
    
