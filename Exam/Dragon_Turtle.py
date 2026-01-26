#the task is to create a chinese dragon using turtle graphics
import turtle

def draw_square(t, size):
    """Draw a square with the given turtle and size."""
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_star(a, size):
    """Draw a star with the given turtle and size."""
    for _ in range(5):
        a.forward(size)
        a.right(144)

def draw_circle(b, radius):
    """Draw a circle with the given turtle and radius."""
    b.circle(radius)

def draw_filled_triangle_on_square(n, square_size, triangle_size, color):
    """Draw a triangle on top of a square and fill it with color."""
    # Draw square
    for _ in range(4):
        n.forward(square_size)
        n.right(90)
    
    # Move to the top of the square
    n.forward(square_size)
    n.right(90)
    n.forward(square_size / 2)
    n.left(90)
    
    # Start filling the triangle
    n.fillcolor(color)
    n.begin_fill()
    
    # Draw triangle
    for _ in range(3):
        n.forward(triangle_size)
        n.left(120)
    
    # End filling the triangle
    n.end_fill()


# --- Example usage ---
screen = turtle.Screen()

# Square
t = turtle.Turtle()
t.penup()
t.goto(-200, 0)   # move square to the left
t.pendown()
draw_square(t, 100)

# Star
a = turtle.Turtle()
a.penup()
a.goto(0, 0)      # center
a.pendown()
draw_star(a, 100)

# Circle
b = turtle.Turtle()
b.penup()
b.goto(200, 0)    # move circle to the right
b.pendown()
draw_circle(b, 50)

# Triangle on square
n = turtle.Turtle()
n.penup()
n.goto(-100, -200)  # move down
n.pendown()
draw_filled_triangle_on_square(n, 100, 100, "blue")

# Only one mainloop at the end
screen.mainloop()