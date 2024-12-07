'''
ITCS 1140 Group Project for Turtle #4
Raymond Connor Zachary Almedin
'''
import turtle as t
import random as r
import time


# Enable RGB mode with 0–255 range DONT EDIT PLEASE its for random colors -AL 
t.colormode(255)


## CONNOR PORTION START ##

# Draws a Circle
def circle():
    t.circle(50)

# Draws a Square
def square():
    for i in range(4):
        t.forward(50)
        t.left(90)

# Draws a Triangle
def triangle():
    for i in range(3):
        t.forward(50)
        t.left(120)

# Draws a Rectangle
def rectangle():
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)

# Draws a Diamond
def diamond():
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(120)

# Draws an upside-down Trapezoid
def inverttrap():
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.right(60)
    t.forward(50)
    t.right(60)
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.right(60)

# Draws a single-line arrow
def arrow():
    t.pensize(5)
    t.forward(100)
    t.left(150)
    t.forward(50)
    t.backward(50)
    t.right(300)
    t.forward(50)

# Draws a Hexagon
def hexagon():
    for i in range(6):
        t.forward(50)
        t.right(60)

# Draws a Pentagon
def pentagon():
    for i in range(5):
        t.forward(100)
        t.left(72)  # 360 / 5

# Draws a spiral
def spiral():
    length = 1
    for i in range(40):
        t.forward(length)
        t.right(90)
        length += 2

## CONNOR PORTION END ##


## ALS PORTION START ##

# List to store shape functions for decision
shapes = [circle, square, triangle, rectangle, diamond, inverttrap, arrow, hexagon, pentagon, spiral]
shape_names = ["circle", "square", "triangle", "rectangle", "diamond", "inverttrap", "arrow", "hexagon", "pentagon", "spiral"]

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
        for i in range(r.randint(1, 6)):  # Generate 1 to 5 random shapes
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

## ALS PORTION END ##

def main():
    print("Welcome to the Turtle Drawing Program!")
    user_choice = input("Do you want random shapes? (Y/N): ")
    user_decision(user_choice)
    print("Thanks for using the program!")
    time.sleep(5)
    t.bye()

main()