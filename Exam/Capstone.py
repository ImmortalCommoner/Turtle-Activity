import turtle

def draw_grid(step):
    t = turtle.Turtle()
    t.speed(0)
    t.color("lightgray")
    for x in range(-300, 301, step):
        t.penup(); t.goto(x, -300); t.pendown(); t.goto(x, 300)
    for y in range(-300, 301, step):
        t.penup(); t.goto(-300, y); t.pendown(); t.goto(300, y)
    t.hideturtle()

draw_grid(50)