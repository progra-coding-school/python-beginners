import turtle

screen = turtle.Screen()
screen.bgcolor("white")   # Set background to white

t = turtle.Turtle()
t.pensize(5)              # Thick lines so kids can see
t.pencolor("red")         # Bright color

for i in range(4):
    t.forward(150)
    t.right(90)

turtle.done()
