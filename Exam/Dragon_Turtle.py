#the task is to create a chinese dragon using turtle graphics
import turtle

def draw_dragon():

    screen = turtle.Screen()
    screen.bgcolor("white")

    dragon = turtle.Turtle()
    dragon.color("blue")
    dragon.pensize(1)
    dragon.speed(10)
    dragon.hideturtle()

    #Draw Dragon Head
    dragon.penup()