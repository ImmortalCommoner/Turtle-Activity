import turtle

t = turtle.Turtle()
t.speed(1000)
screen = turtle.Screen()
t.penup()
t.goto(-100, -100)


def draw_megaman():
    
    #first row
    for _ in range(9):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    t.pu()
    t.forward(30)
    t.pd()

    for _ in range(9):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    #second row
    t.pu()
    t.goto(-100, -90)

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(7):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    t.pu()
    t.forward(30)
    t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(7):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #third row

    t.pu()
    t.goto(-90,-80)
    t.pd()

    for _ in range(2):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(6):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    t.pu()
    t.forward(30)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(3):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(3):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    #fourth row
    t.pu()
    t.goto(-70,-70)
    t.pd()

    for _ in range(2):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(3):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(2):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    t.penup()
    t.forward(20)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(4):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #fifth row
    t.pu()
    t.goto(-50,-60)
    t.pu()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(4):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(2):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(3):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(2):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    #sixth row
    t.pu()
    t.goto(-40,-50)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(3):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(4):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(3):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
        
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #seventh row
    t.pu()
    t.goto(-30,-40)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(6):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #eight row
    t.pu()
    t.goto(-20,-30)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(7):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    #ninth row
    t.pu()
    t.goto(-30,-20)
    t.pd()
    
    for _ in range(2):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(2):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(5):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #tenth row
    t.pu()
    t.goto(-40,-10)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(2):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(7):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #eleventh row
    t.pu()
    t.goto(-50,0)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(4):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(7):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(5):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    t.pu()
    t.forward(10)
    t.pd()

    for _ in range(4):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #twelveth row
    t.pu()
    t.goto(-60,10)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(2):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(2):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(2):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(5):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(5):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(3):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(3):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #13th row
    t.pu()
    t.goto(-70,20)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(3):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(2):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(5):
        t.fillcolor("sandy brown")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(4):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(4):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #14th row
    t.pu()
    t.goto(-70,30)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(3):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(2):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("sandy brown")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(4):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("sandy brown")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(2):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(2):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(3):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #15th row
    t.pu()
    t.goto(-70,40)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(5):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(2):
        t.fillcolor("sandy brown")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(3):
        t.fillcolor("white")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("sandy brown")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("white")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("sandy brown")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(4):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(3):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(3):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #16th row
    t.pu()
    t.goto(-60,50)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(5):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("sandy brown")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(2):
        t.fillcolor("white")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(2):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("sandy brown")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("white")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    t.pu()
    t.forward(30)
    t.pd()

    for _ in range(4):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #17th row
    t.pu()
    t.goto(-50,60)
    t.pd()

    for _ in range(2):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(2):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("sandy brown")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(2):
        t.fillcolor("white")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(2):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("sandy brown")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("white")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #18th row
    t.pu()
    t.goto(-30,70)
    t.pd()

    for _ in range(3):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(2):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
                
    for _ in range(1):
        t.fillcolor("sandy brown")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(3):
        t.fillcolor("white")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(2):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("white")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #19th row
    t.pu()
    t.goto(-10,80)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(6):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(2):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
        
    #20th row
    t.pu()
    t.goto(0,90)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
        
    for _ in range(5):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(2):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #21th row
    t.pu()
    t.goto(0,100)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
        
    for _ in range(5):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(4):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    #22th row
    t.pu()
    t.goto(10,110)
    t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
        
    for _ in range(3):
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(2):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    #23th row
    t.pu()
    t.goto(20,120)
    t.pd()

    for _ in range(3):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
        
    for _ in range(2):
        t.fillcolor("light blue")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
    
    for _ in range(1):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()

    #24th row
    t.pu()
    t.goto(40,130)
    t.pd()

    for _ in range(3):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):           
            t.forward(10)
            t.right(90)
        t.end_fill()

        t.penup()
        t.forward(10)
        t.pd()
        
    

draw_megaman()
screen.mainloop()