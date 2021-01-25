import math
import turtle
import Polygon #módulo polígono

bob = turtle.Turtle()
def circle(t, r):
    circunference = 2 * math.pi * r
    n = int(circunference / 3) + 1
    length = circunference / n
    Polygon.polygon(t, n, length) #argumentos para função
#turtle.mainloop()
circle(bob, 100)
