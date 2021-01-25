import turtle           
def square(length, count):
    i = 0
    bob = turtle.Turtle()
    while i <= count:
        i = i + 1           
        for c in range(4):                        
            bob.fd(length)                                     
            bob.lt(90)
        for c in range(4):                        
            bob.fd(length)                                     
            bob.rt(90)
        for c in range(4):                        
            bob.bk(length)                                     
            bob.lt(90)
        for c in range(4):                        
            bob.bk(length)                                     
            bob.rt(90)
        bob.fd(length)
        bob.lt(135)
        for c in range(4):
            bob.fd(length*(2**(1/2)))                                     
            bob.lt(90)
        bob.rt(135)
        bob.fd(length)
    turtle.mainloop()
square(50, 3)

