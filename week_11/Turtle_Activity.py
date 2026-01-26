import turtle

def draw_square(t, size):
    """Draw a square with the given turtle and size."""
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Example usage
screen = turtle.Screen()
t = turtle.Turtle()
draw_square(t, 100)
screen.mainloop()
