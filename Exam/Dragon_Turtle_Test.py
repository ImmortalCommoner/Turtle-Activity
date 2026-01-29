import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")

def headshape(
        a=-1,
        b=1,
        c=12,
        d=5,
        e=5,
        f=0):
    t.penup()
    t.setposition(-70,-5)
    t.right(10)
    if b==1:
        t.pendown()
        if f==0:
            t.begin_fill()
    t.forward(220)
    if b>=2:
        t.pendown()
        if f==0:
            t.begin_fill()
    if a >= 0:
        t.circle(5,80)
    if a >= 1:
        t.circle(60,100)
    if a >= 2:
        t.left(195)
        for i in range(c):
            t.circle(130,-5)
    if a >= 3:    
        t.left(180)
        for i in range(d):
            t.circle(75,10)
    if a >= 4:    
        t.right(3)    
        t.forward(45)
    if a >= 5:
        t.circle(10,100)
    if a >= 6:
        t.forward(3)
        for i in range(e):
            t.forward(10)
    if a >= 7:
        t.circle(30,35)
        t.forward(60)    
        t.circle(30,35)
        t.left(18)


#get turtle out of the way
t.speed(0)
t.penup()
t.setposition(200,200)

screen.mainloop()