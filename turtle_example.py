# Start by importing the turtle module:
import turtle

# Setting up the background
bg = turtle.Screen() # Creates background
bg.title("Playing with Turtle") # setting the title
bg.bgcolor('light blue') # setting the color 
bg.setup(width=600, height=600) # setting the boundaries

# Setting up our turtle
f = turtle.Pen() # Creates the turtle
f.color("red") # Setting the pen color red

# make a triangle
f.fd(100)
f.left(120)
f.fd(100)
f.left(120)
f.fd(100)

f.left(30)
# make a square
f.penup()
f.fd(50)
f.pendown()

f.fd(100)
f.left(90)
f.fd(100)
f.left(90)
f.fd(100)
f.left(90)
f.fd(100)

# Moving turtle
#steps = 1000

# while (steps > 0):
 #   f.left(30)
  #  f.forward(40)
   # f.left(20)
    #f.forward(50)
    #f.right(21)
    #f.forward(24)
    #steps = steps + 1






