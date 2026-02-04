# num1 = 0
# def sqrCubeNum():
#     num1 = int(input("Enter a number: "))
#     return num1, num1*num1, num1*num1*num1

# num1, sqr, cube = sqrCubeNum()
# print("SQR of ", num1, "is: ", sqr)
# print("Cube of ", num1, "is: ", cube)

# num1=int(input("Enter a num1: "))
# num2=int(input("Enter a num2: "))

import turtle

# --- Configuration ---
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
screen = turtle.Screen()
screen.setup(CANVAS_WIDTH, CANVAS_HEIGHT)
screen.title("Multi-Turtle 3D Cube")
screen.bgcolor("white")

def gimp_to_turtle(gimp_x, gimp_y):
    """Converts GIMP (top-left 0,0) to Turtle (center 0,0)"""
    turtle_x = gimp_x - (CANVAS_WIDTH / 2)
    # The y-axis is inverted: positive up for turtle, positive down for gimp
    turtle_y = (CANVAS_HEIGHT / 2) - gimp_y 
    return turtle_x, turtle_y

# --- Turtle Setup ---

# Turtle for the FRONT Face
front_face = turtle.Turtle()
front_face.color("blue", "lightblue")
front_face.pensize(2)
front_face.speed(1) # Slowed down so you can watch them work

# Turtle for the SIDE/TOP Faces
side_face = turtle.Turtle()
side_face.color("red", "lightcoral")
side_face.pensize(2)
side_face.speed(1) 


# --- Drawing Logic ---

# Coordinates plotted in GIMP for a 200x200 pixel front face, 
# starting around the center of our 800x600 canvas (GIMP coords)
FRONT_SQUARE_POINTS = [
    (300, 200), # Bottom Left
    (500, 200), # Bottom Right
    (500, 400), # Top Right
    (300, 400), # Top Left
    (300, 200)  # Back to Start
]

# Coordinates for the side/top faces (connected to the front points)
# Uses the same top right and top left points as the front face
SIDE_POINTS_SEQUENCE = [
    (500, 400), # Start from Front's Top Right
    (600, 500), # Back Top Right (angled back and up)
    (400, 500), # Back Top Left
    (300, 400), # Back to Front's Top Left
]


# Draw the Front Face
front_face.penup()
front_face.goto(gimp_to_turtle(*FRONT_SQUARE_POINTS[0]))
front_face.pendown()
front_face.begin_fill()
for point in FRONT_SQUARE_POINTS:
    front_face.goto(gimp_to_turtle(*point))
front_face.end_fill()


# Draw the Side and Top Faces
side_face.penup()
# Start drawing from the front's top right corner
side_face.goto(gimp_to_turtle(*SIDE_POINTS_SEQUENCE[0])) 
side_face.pendown()
side_face.begin_fill()

for point in SIDE_POINTS_SEQUENCE:
    side_face.goto(gimp_to_turtle(*point))

side_face.end_fill()

# Finish connecting the last bottom edge from back to front
side_face.penup()
side_face.goto(gimp_to_turtle(400, 500)) # Back Top Left
side_face.pendown()
side_face.goto(gimp_to_turtle(400, 300)) # Back Bottom Left (Need a custom point not in the list)
side_face.goto(gimp_to_turtle(300, 200)) # Connect to Front Bottom Left


# Keep the window open
turtle.done()
