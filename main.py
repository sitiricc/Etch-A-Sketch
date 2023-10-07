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
    # displays the keys for user to see
    etchy.penup()
    etchy.goto(-301, -299) 
    etchy.write("'w': forward, 's':backward, 'a': counter-clockwise, 'd': clockwise, 'c': clear the screen.", align="left", font=("Arial", 9, "normal"))
    etchy.penup()
    etchy.goto(0, 0)  # Return to the starting position
    etchy.pendown()

def random_color():
    # picks random color for etch-a-sketch
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#{:02X}{:02X}{:02X}".format(r, g, b)  # Convert RGB to hexadecimal


def move_forwards():
    # Function to set the turtle's color and then move forward
    initial_color = random_color()
    etchy.color(initial_color)
    etchy.forward(10)


def move_backwards():
    # Function to set the turtle's color and then move backward
    initial_color = random_color()
    etchy.color(initial_color)
    etchy.backward(10)

def counter_clockwise():
    # Function to set the turtle's color and then move counter clockwise
    initial_color = random_color()
    etchy.color(initial_color)
    etchy.left(10)
    etchy.forward(10)

def clockwise():
    # Function to set the turtle's color and then move backward
    initial_color = random_color()
    etchy.color(initial_color)
    etchy.right(10)
    etchy.forward(10)

def clear_screen():
    # Function to clear screen
    etchy.clear()
    etchy.penup()
    etchy.home()
    etchy.pendown()

# Key display and user answers
display_key_info()
screen.listen()
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="d", fun=clockwise)

# Code to bring up screen
screen.exitonclick()
