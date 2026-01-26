import turtle

# def draw_square(t, size):
#     """Draw a square with the given turtle and size."""
#     for _ in range(4):
#         t.forward(size)
#         t.right(90)

# # Example usage
# screen = turtle.Screen()
# t = turtle.Turtle()
# draw_square(t, 100)

# """Draw a star with the given turtle and size."""
# def draw_star(a, size):
#     for _ in range(5):
#         a.forward(size)
#         a.right(144)

# # Example usage
# screen = turtle.Screen()
# a = turtle.Turtle()
# draw_star(a, 100)

# """Draw a circle with the given turtle and radius."""
# def draw_circle(b, radius):
#     b.circle(radius)

# # Example usage
# screen = turtle.Screen()
# b = turtle.Turtle()
# draw_circle(b, 50)

# """Draw a triangle on top of a square and fill it with color."""

# def draw_filled_triangle_on_square(n, square_size, triangle_size, color):
#     # Draw square
#     for _ in range(4):
#         n.forward(square_size)
#         n.right(90)
    
#     # Move to the top of the square
#     n.forward(square_size)
#     n.right(90)
#     n.forward(square_size / 2)
#     n.left(90)
    
#     # Start filling the triangle
#     n.fillcolor(color)
#     n.begin_fill()
    
#     # Draw triangle
#     for _ in range(3):
#         n.forward(triangle_size)
#         n.left(120)
    
#     # End filling the triangle
#     n.end_fill()

# # Example usage
# screen = turtle.Screen()
# n = turtle.Turtle()
# draw_filled_triangle_on_square(n, 100, 100, "blue")


# def draw_filled_triangle_on_square(g, square_size, triangle_size, square_color, triangle_color):
#     # Draw filled square
#     g.fillcolor(square_color)
#     g.begin_fill()
#     for _ in range(4):
#         g.forward(square_size)
#         g.right(90)
#     g.end_fill()
    
#     # Move to the top of the square
#     g.forward(square_size)
#     g.right(90)
#     g.forward(square_size / 2)
#     g.left(90)
    
#     # Draw filled triangle
#     g.fillcolor(triangle_color)
#     g.begin_fill()
#     for _ in range(3):
#         g.forward(triangle_size)
#         g.left(120)
#     g.end_fill()

# # Example usage
# screen = turtle.Screen()
# g = turtle.Turtle()
# draw_filled_triangle_on_square(g, 100, 100, "blue", "red")


# def draw_filled_triangle_on_square(n, square_size, triangle_size, square_color, triangle_color):
#     # Draw filled square
#     n.fillcolor(square_color)
#     n.begin_fill()
#     for _ in range(4):
#         n.forward(square_size)
#         n.right(90)
#     n.end_fill()
    
   
#     # Draw filled triangle
#     n.fillcolor(triangle_color)
#     n.begin_fill()
#     for _ in range(3):
#         n.forward(triangle_size)
#         n.left(120)
#     n.end_fill()

# # Example usage
# screen = turtle.Screen()
# n = turtle.Turtle()
# draw_filled_triangle_on_square(n, 100, 100, "red", "blue")

# screen.mainloop()
