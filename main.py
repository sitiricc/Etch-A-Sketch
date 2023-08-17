from turtle import *
from art import *

# w foward
# s backward
# a counter-clockwise
# d clockwise
# c clear drawing


etchy= Turtle()
screen= Screen()


# functions to move mouse
def move_forwards():
    etchy.forward(10)

def move_backwards():
    etchy.backward(10)

def counter_clockwise():
    etchy.left(10)
    etchy.forward(10)

def clockwise():
    etchy.right(10)
    etchy.forward(10)

def clear_screen():
    etchy.clear()
    etchy.penup()
    etchy.home()
    etchy.pendown()




# user answers
screen.listen()
screen.onkey(key= "s", fun= move_backwards)
screen.onkey(key= "w", fun= move_forwards)
screen.onkey(key= "a", fun= counter_clockwise)
screen.onkey(key= "c", fun= clear_screen)
screen.onkey(key= "d", fun= clockwise)



# Code to bring up screen
screen.exitonclick()