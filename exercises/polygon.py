import turtle
bob = turtle.Turtle()
def polygon(length, side):
    bob = turtle.Turtle()
    x = 180*(side-2)
    angle = 180-(x/side)
    for i in range(side):
        bob.fd(length)
        bob.lt(angle)
    turtle.mainloop()
side = int(input("Digite o números de lados do polígono: "))
length = int(input("Agora digite o tamanho em pixels da figura: "))
polygon(length, side)
