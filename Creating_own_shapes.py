from turtle import Turtle, Screen
import random
tom = Turtle()
colours = ['CornflowerBlue','DarkOrchid','IndianRed','DeepSkyBlue','LightSeaGreen','Wheat','SlateGrey']
tom.color("blue")
# 'CornflowerBlue','DarkOrchid','IndianRed','DeepSkyBlue','LightSeaGreen','Wheat','SlateGrey'
tom.width(5)

# use
# W - FORWARD
# S - BACKWORD
# A -LEFT
# D - RIGHT
# AND TWO KEYS SIMULATNEOUSLY FOR ANGLE SETTING
def forward():
    tom.forward(10)
    tom.color(random.choice(colours))


def backword():
    tom.backward(5)
    tom.color(random.choice(colours))


def right():
    heading = tom.heading() + 10
    tom.setheading(heading)
    tom.color(random.choice(colours))


def left():
    heading = tom.heading() - 10
    tom.setheading(heading)
    tom.color(random.choice(colours))


def clear():
    tom.clear()
    tom.penup()
    tom.reset()
    tom.pendown()

screen = Screen()
screen.listen()
screen.onkey(key='w',fun=forward)
screen.onkey(key='s',fun=backword)
screen.onkey(key='d',fun=right)
screen.onkey(key='a',fun=left)
screen.onkey(key='c',fun=clear)
screen.exitonclick()
