import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)

h = 0

for i in range(180):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)

    # Draw a star
    for j in range(5):
        t.forward(200)
        t.right(144)

    # Rotate the star
    t.right(2)

    h += 0.005

turtle.done()
