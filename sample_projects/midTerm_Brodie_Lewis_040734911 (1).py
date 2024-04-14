import turtle

"""
- Author(s) Nikita Silaparasetty 
- Title of program/source code: The Beginner's Guide to Python Turtle
- Code version: Python3 
- Type: Guide/source code
- Availability: https://shorturl.at/vwyZ5

"""
screen = turtle.Screen()


# Define the draw_square function with coordinates
def draw_square(size, x, y):
    # Create a turtle named 'my_turtle'
    my_turtle = turtle.Turtle()

    # Move the turtle to the specified coordinates
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

    # Draw a square with the specified size of 7 units
    for _ in range(7):
        my_turtle.forward(size)
        my_turtle.right(90)


# Define the draw_triangle function with coordinates
def draw_triangle(size, x, y):
    # Create a turtle named 'my_turtle'
    my_turtle = turtle.Turtle()

    # Lifts pen up and down from the drawing screen and moves the turtle to the specified coordinates
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

    # Draw a triangle with the specified size of 7 units
    for _ in range(7):
        my_turtle.forward(size)
        my_turtle.right(120)


# Lifts pen up and down from the drawing screen and moves the turtle to the specified coordinates
def draw_circle(size, x, y):
    my_turtle = turtle.Turtle()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

    # Draw a black circle with the specified size of 7 units
    for _ in range(7):
        my_turtle.dot(size)


# Draw a square, trianlge and black dot
draw_square(50, -50, 50)
draw_triangle(50, 50, 50)
draw_circle(20, -60, 60)

# Keeps the window open
turtle.done()
