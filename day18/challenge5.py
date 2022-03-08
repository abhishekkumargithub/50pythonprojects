import random
from turtle import Turtle,Screen

from scipy import rand

tim=Turtle()


def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

tim.speed("fastest")

tim.color(random_color())
tim.circle(100)
current_heading=tim.heading()
tim.setheading(current_heading*10)
tim.circle(100)



screen=Screen()
screen.exitonclick()