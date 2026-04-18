import tkinter as tk

root = tk.Tk()
root.tk.call('tk', 'scaling', 2.0)
root.destroy()

import turtle
import random

screen = turtle.Screen()
screen.title("Static Electricity ⚡")
screen.bgcolor("white")
screen.setup(width=900, height=600)

balloon = turtle.Turtle()
balloon.shape("circle")
balloon.color("red")
balloon.penup()

papers = []

for _ in range(15):
    p = turtle.Turtle()
    p.shape("circle")
    p.color("blue")
    p.shapesize(1, 1)
    p.penup()
    p.goto(random.randint(-300, 300), random.randint(-200, 200))
    papers.append(p)


def attract():
    for p in papers:
        x, y = p.xcor(), p.ycor()
        bx, by = balloon.xcor(), balloon.ycor()

        p.setx(x + (bx - x) * 0.05)
        p.sety(y + (by - y) * 0.05)

    screen.ontimer(attract, 50)


def move_balloon(x, y):
    balloon.goto(x, y)


screen.onscreenclick(move_balloon)

attract()

screen.mainloop()