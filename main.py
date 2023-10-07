from turtle import *
import random

# w forward
# s backward
# a counter-clockwise
# d clockwise
# c clear drawing

etchy = Turtle()
screen = Screen()


def display_key_info():
    etchy.penup()
    etchy.goto(-301, -299)  # Adjust the coordinates as needed
    etchy.write("'w': forward, 's':backward, 'a': counter-clockwise, 'd': clockwise, 'c': clear the screen.", align="left", font=("Arial", 9, "normal"))
    etchy.penup()
    etchy.goto(0, 0)  # Return to the starting position
    etchy.pendown()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#{:02X}{:02X}{:02X}".format(r, g, b)  # Convert RGB to hexadecimal

# Function to set the turtle's color and then move forward
def move_forwards():
    initial_color = random_color()
    etchy.color(initial_color)
    etchy.forward(10)

# Function to set the turtle's color and then move backward
def move_backwards():
    initial_color = random_color()
    etchy.color(initial_color)
    etchy.backward(10)

def counter_clockwise():
    initial_color = random_color()
    etchy.color(initial_color)
    etchy.left(10)
    etchy.forward(10)

def clockwise():
    initial_color = random_color()
    etchy.color(initial_color)
    etchy.right(10)
    etchy.forward(10)

def clear_screen():
    etchy.clear()
    etchy.penup()
    etchy.home()
    etchy.pendown()

# User answers

display_key_info()
screen.listen()
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="d", fun=clockwise)

# Code to bring up screen
screen.exitonclick()
