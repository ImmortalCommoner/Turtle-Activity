import turtle

CANVAS_HEIGHT = 700
CANVAS_WIDTH = 1000

screen = turtle.Screen()
screen.setup(CANVAS_WIDTH, CANVAS_HEIGHT)
screen.bgcolor("white")

def coordinates(x, y):
    turtle_x = x - (CANVAS_WIDTH / 2)
    turtle_y = (CANVAS_HEIGHT / 2) - y 
    return turtle_x, turtle_y


t = turtle.Turtle()

buildingPoints = [
    (900, 96),
    (564, 103),
    (551, 257),
    (559, 258),
    (553, 326),
    (560, 327)

]

def draw_building():

    t.pu()
    t.goto(coordinates(*buildingPoints[0]))
    t.pd()
    for point in buildingPoints:
        t.goto(coordinates(*point))

    




draw_building()
screen.mainloop()