def rightJustify(string):
    x = len(string)
    y = 70 - x
    print((y * " ")+ string)
string = input("Digite uma frase: ")
rightJustify(string)
