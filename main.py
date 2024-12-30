'''
Group Project for Turtle #4
Raymond Connor Zachary Almedin
'''
import turtle as t
import random as r
import time

## RAYMOND'S PORTION START (12/7/2024) ##

# Creating the turtle
t.shape("turtle")
t.color("green")
t.pensize(5)
t.home()

# Setting up the screen
s = t.Screen()
s.title("Random Shapes")
s.setup(width = 800, height = 600)
s.bgcolor("blue")

# Enable RGB mode with 0–255 range DONT EDIT PLEASE its for random colors -AL 
t.colormode(255)

## RAYMOND'S PORTION END ##

## CONNOR PORTION START ##

# Draws a Circle
def circle():
    radius = r.randint(20, 100)  # Random radius
    t.circle(radius)

# Draws a Square
def square():
    side = r.randint(20, 100)  # Random side length
    for i in range(4):
        t.forward(side)
        t.left(90)

# Draws a Triangle
def triangle():
    side = r.randint(20, 100)
    for i in range(3):
        t.forward(side)
        t.left(120)

# Draws a Rectangle
def rectangle():
    width = r.randint(50, 150)  # Random width
    height = r.randint(20, 100)  # Random height
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Draws a Diamond
def diamond():
    diagonal1 = r.randint(50, 150)  # Random diagonal lengths
    diagonal2 = r.randint(50, 150)
    t.forward(diagonal1 / 2)
    t.left(60)
    t.forward(diagonal2)
    t.left(120)
    t.forward(diagonal1)
    t.left(120)
    t.forward(diagonal2)
    t.left(60)
    t.forward(diagonal1 / 2)

# Draws an upside-down Trapezoid
def inverttrap():
    base = r.randint(50, 100)  # Random base size
    top = base // 2  # Smaller top for trapezoid
    height = r.randint(30, 70)
    t.forward(base)
    t.right(120)
    t.forward(height)
    t.right(60)
    t.forward(top)
    t.right(60)
    t.forward(height)
    t.right(120)

# Draws a single-line arrow
def arrow():
    length = r.randint(50, 150)  # Random arrow length
    head = length // 3  # Arrowhead size
    t.pensize(5)
    t.forward(length)
    t.left(150)
    t.forward(head)
    t.backward(head)
    t.right(300)
    t.forward(head)

# Draws a Hexagon
def hexagon():
    side = r.randint(20, 100)
    for i in range(6):
        t.forward(side)
        t.right(60)


# Draws a Pentagon
def pentagon():
    side = r.randint(30, 100)
    for i in range(5):
        t.forward(side)
        t.left(72)

# Draws a spiral
def spiral():
    length = 1
    increment = r.randint(1, 5)
    for i in range(40):
        t.forward(length)
        t.right(90)
        length += increment

## CONNOR PORTION END ##

## ZACHARY PORTION START ##

#Star shape
def star():
    side = r.randint(30, 100)
    for i in range(5):
        t.forward(side)
        t.right(144)

#Cross shape
def cross():
    for i in range(4):
        t.fd(50)
        t.right(90)
        t.fd(50)
        t.left(90)
        t.fd(50)
        t.left(90)

#Semicircle shape (The best I could get)
def semicircle():
    #Drawing out half of the circle's circ
    for i in range(180):
        t.forward(1)
        t.right(1)
    #Turn to draw the line, 90 to the right because we are exactly flipped from the start
    t.right(90)
    #Drawing to fit the line to the dia. Circumference(360)/pi(half of the circle) ~= 115
    t.forward(115)


## ZACHARY PORTION END ##

## ALMEDIN PORTION START ##

# List to store shape functions for decision
shapes = [circle, square, triangle, rectangle, diamond, inverttrap, arrow, hexagon, pentagon, spiral, star, cross, semicircle]
shape_names = ["circle", "square", "triangle", "rectangle", "diamond", "inverttrap", "arrow", "hexagon", "pentagon", "spiral", "star", "cross", "semicircle"]

# Selects a random shape and draws it
def random_shape():
    t.penup()
    t.goto(r.randint(-200, 200), r.randint(-200, 200))  # Move to a random position
    t.pendown()
    t.setheading(r.randint(0, 360))  # Set a random rotation angle
    t.color(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))  # Set random color
    r.choice(shapes)()

# Handles user decision for random or specific shapes
def user_decision(user_choice):
    if user_choice.upper() == "Y":  # Random shapes
        for i in range(r.randint(1, 11)): # generate 1 to 10 random shapes
            random_shape()
    elif user_choice.upper() == "N":  # User-selected shapes
        user_shapes = ""
        while user_shapes.upper() != "Q":  # Loop until user quits
            print("\nAvailable Shapes:")
            for shape in shape_names:
                print(f"- {shape}")
            user_shapes = input("Enter the shape (or Q to quit): ").lower()
            if user_shapes in shape_names:  # Check if the input matches
                shape_index = shape_names.index(user_shapes)
                t.penup()
                t.goto(r.randint(-200, 200), r.randint(-200, 200))  # Move to a random position
                t.setheading(r.randint(0, 360))  # Set a random rotation angle
                t.color(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))  # Set random color
                t.pendown()
                shapes[shape_index]()  # Call the selected shape function
            elif user_shapes.upper() != "Q":
                print("Invalid shape. Please choose a shape from the list or enter Q to quit.")

## ALMEDIN PORTION END ##

def main():
    print("Welcome to the Turtle Drawing Program!")
    user_choice = input("Do you want random shapes? (Y/N): ")
    user_decision(user_choice)
    print("Thanks for using the program!")
    time.sleep(5)
    t.bye()

main()
