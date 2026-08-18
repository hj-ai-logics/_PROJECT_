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
for i in range(400):
  color = colorsys.hsv_to_rgb(h, 1, 1)
  t.pencolor(color)
  t.forward(i)
  t.left(121)
  h += 0.005

turtle.done()




