'''
ITCS 1140 Group Project for Turtle #4
Raymond Connor Zachary Almedin
'''
import turtle as t
import random as r



## ALS PORTION START ##

# list to store shape functions for decision
shapes = [square, circle, triangle, star, hexagon]
shape_names = ["square", "circle", "triange", "star", "hexagon"] #corresponding names

#selects a random shape and adds () to the end, made it a seperate function to be able to call it in a randomized loop
def random_shape():
    r.choice(shapes)()

# If structure for user's choice if they want random shapes (Y/N)
def user_decision(user_choice): # takes the users inputs as param for if structure
    if user_choice.upper() == "Y": # random shapes
        for i in range(r.int(1, 6)): # generate 1 to 5 random shapes
            #i put more in here later - AL (11/18/24)
    elif user_choice.upper() == "N": # user selected shapes
        user_shapes = ""
        while user_shapes.upper() != "Q": #loop until user quits
            print("Available Shapes: /n square /n circle")
            user_shapes = input("Enter the shape ( or Q to quit): ").lower()
            if user_shapes in shape_names: # check if the input matches
                #i put more in here later - AL (11/18/24)
            else:
                print("Invalid shape. Please choose a shape from the list or enter Q to quit")
            
## ALS PORTION END ##




def main():
    user_decision(user_choice)

main()