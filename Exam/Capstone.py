import turtle

CANVAS_HEIGHT = 3100
CANVAS_WIDTH = 4100

screen = turtle.Screen()
screen.setup(CANVAS_WIDTH/6, CANVAS_HEIGHT/6)
screen.bgcolor("white")


def coordinates(x, y):
    turtle_x = (x - (CANVAS_WIDTH / 2))/6
    turtle_y = ((CANVAS_HEIGHT / 2) - y)/6
    return turtle_x, turtle_y


t = turtle.Turtle()
t.speed(0)
t.hideturtle

buildingPoints = [
    (4095.96, 3071.61),
  	(4095.96, 2147.62),
  	(3831.92, 3071.61),
  	(4095.96, 3071.61),
  	
]

bottomRightBeamPoints = [
    (4095.96, 2147.62),
    (4095.96, 1952.17),
    (3729.63, 3071.61),
    (3831.92, 3071.61),
    (4095.96, 2147.62),
  	
]

bottomTopBeamPoints = [
    (4095.96, 1952.17),
    (4095.96, 1628.74),
    (3981.98, 1618.58),
    (3084.55, 3071.61),
    (3729.63, 3071.61),
    (4095.96, 1952.17),
      	
]

RightColumnPoints = [
    (4095.96, 1062.77),
    (4095.96, 1628.74),
    (3981.98, 1618.58),
    (3690.57, 2091.09),
    (3765.94, 1058.84),
    (3844.04, 1034.78),
    (4095.96, 1033.54),
    (4095.96, 1062.54),
    (3765.94, 1058.78),
]

def draw_building():

    # yellow gutter
    t.pu()
    t.goto(coordinates(*buildingPoints[0]))
    t.pd()
    
    t.fillcolor("yellow")
    t.begin_fill()
    for point in buildingPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    # column
    t.pu()
    t.goto(coordinates(*bottomRightBeamPoints[0]))
    t.pd()
    
    t.fillcolor("gray")
    t.begin_fill()
    for point in bottomRightBeamPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()
    
    t.pu()
    t.goto(coordinates(*bottomTopBeamPoints[0]))
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for point in bottomTopBeamPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    # Right Column

    t.pu()
    t.goto(coordinates(*RightColumnPoints[0]))
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for point in RightColumnPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    




draw_building()
screen.mainloop()