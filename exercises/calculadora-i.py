#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=--=-=#
#=-=-=-=-=-=-Definição de algumas BIBLIOTECAS:=-=-=-=-=-=-=-=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=--=-=#
from tkinter import *
from math import *
#-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=#
janela = Tk()                       #Instancia padrao
janela.title("CALCULADORA")         #Definição do titulo
janela.geometry("330x330+400+100")  #Definição da geometria
janela["background"]="silver"       #Definição de cor de fundo
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=--=-=#
#=-=-=-=-=-=-Definição de algumas VARIÁVEIS:=-=-=-=-=-=-=-=-=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=--=-=#
l = 10 #Largura do botão.
margem_topo1 = 10 #Distancia até a margem superior para os Labels.
margem_topo2 = 40
margem_topo3 = 70
operador = []
operator = []
numero1 = []
numero2 = []
valores = []
raiz = []
quant = len(operador)
num1 = 0
num2 = 0
resultado = [0]
c1 = 300 #Camada 1, contando de baixo para cima.
c2 = 265 #Camada 2, contando de baixo para cima.
c3 = 230 #Camada 3, contando de baixo para cima.
c4 = 195 #Camada 4, contando de baixo para cima.
c5 = 160 #Camada 5, contando de baixo para cima.
c6 = 125 #Camada 6, contando de baixo para cima.
a, b, c, d = 5, 85, 165, 245
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=#
#-=-=--=Definição das FUNÇÕES da calculadora.=--=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=#
def pi_btn():
    if (len(operador) == 0):
        numero1.append(3.1415926536)
    else:
        numero2.append(3.1415926536)
    print(quant)
def zero():
    if len(operador) == 0:
        numero1.append(0)
    else:
        numero2.append(0)
def point():
    print()
def one():
    if len(operador) == 0:
        numero1.append(1)
    else:
        numero2.append(1)
def two():
    if len(operador) == 0:
        numero1.append(2)
    else:
        numero2.append(2)
def three():
    if len(operador) == 0:
        numero1.append(3)
    else:
        numero2.append(3)
def four():
    if len(operador) == 0:
        numero1.append(4)
    else:
        numero2.append(4)
def five():
    if len(operador) == 0:
        numero1.append(5)
    else:
        numero2.append(5)
def six():
    if len(operador) == 0:
        numero1.append(6)
    else:
        numero2.append(6)
def seven():
    if len(operador) == 0:
        numero1.append(7)
    else:
        numero2.append(7)
def eight():
    if len(operador) == 0:
        numero1.append(8)
    else:
        numero2.append(8)
def nine():
    if len(operador) == 0:
        numero1.append(9)
    else:
        numero2.append(9)
def plus():
    operador.append(1)
def minus():
    operador.append(2)
def times():
    operador.append(3)
def divide():
    operador.append(4)
def raiz_funccion():
    raiz.append(1)
    print(raiz)
def clear():
    operador.clear()
    numero1.clear()
    numero2.clear()
    valores.clear()
    resultado.clear()
    labels_iniciais()
    return 0
def equal():
    valor_um = 0
    valor_dois = 0
    expoente_um = (len(numero1)-1)              #Índice da base dez a ser multiplicada.
    expoente_dois = (len(numero2)-1)            #
    for c in numero1:                           #PRIMEIRO número digitado:
        valor_um += (c * (10**expoente_um))           
        expoente_um -= 1
        
    for c in numero2:                           #SEGUNDO número digitado:
        valor_dois += (c * (10**expoente_dois))           
        expoente_dois -= 1
    valores.append(valor_um)
    valores.append(valor_dois)
    operadores()
def operadores():
    if (operador[len(operador)-1] == 1):
        resul = (valores[0] + valores[1])
        operator.append("+")
    elif (operador[len(operador)-1] == 2):
        resul =(valores[0] - valores[1])
        operator.append("-")
    elif (operador[len(operador)-1] == 3):
        resul =(valores[0] * valores[1])
        operator.append("X")
    elif (operador[len(operador)-1] == 4):
        resul =(valores[0] / valores[1])
        operator.append("/")
    elif (len(raiz_funccion )!= 0):
        resul = valores[0]**(1/2)
        operador.append(5)
    resultado.append(resul)
    
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=#
    #-=-=-=-=Definição dos Labels da calculadora.=--=-=#
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=#
    lb_one = Label(janela, text = valores[0])
    lb_two = Label(janela, text = valores[1])
    lb_three = Label(janela, text = resultado[-1])
    lb_operator = Label(janela, text = operator[-1])
    lb_equal = Label(janela, text = " = ")

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=--=#
    #Definição do posicionamento dos Labels com gerenciador PLACE.
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    lb_one.place(x = a, y = margem_topo1)
    lb_two.place(x = a, y = margem_topo2)
    lb_three.place(x = a, y = margem_topo3)
    lb_operator.place(x = 300, y = margem_topo1)
    lb_equal.place(x = 295, y = margem_topo2)
    print(resultado)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=#
#-=-=-=-=Definição dos BOTÕES da calculadora.=--=-=#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=#
bt_pi = Button(janela, width = l, text = "Π", command = pi_btn)
bt_zero = Button(janela, width = l, text = "0", command = zero)
bt_point = Button(janela, width = l, text = ".", command = point)
bt_equal = Button(janela, width = l, text = "=", command = equal)
bt_one = Button(janela, width = l, text = "1", command = one)
bt_two = Button(janela, width = l, text = "2", command = two)
bt_three = Button(janela, width = l, text = "3", command = three)
bt_plus = Button(janela, width = l, text = "+", command = plus)
bt_four = Button(janela, width = l, text = "4", command = four)
bt_five = Button(janela, width = l, text = "5", command = five)
bt_six = Button(janela, width = l, text = "6", command = six)
bt_minus = Button(janela, width = l, text = "-", command = minus)
bt_seven = Button(janela, width = l, text = "7", command = seven)
bt_eigh = Button(janela, width = l, text = "8", command = eight)
bt_nine = Button(janela, width = l, text = "9", command = nine)
bt_times = Button(janela, width = l, text = "X", command = times)
bt_ce = Button(janela, width = l, text = "CE")
bt_c = Button(janela, width = l, text = "C", command = clear)
bt_back = Button(janela, width = l, text = "BACK")
bt_divide = Button(janela, width = l, text = "÷", command = divide)
bt_per = Button(janela, width = l, text = "%")
bt_raiz = Button(janela, width = l, text = "√", command = raiz_funccion)
bt_square = Button(janela, width = l, text = "X²")
bt_div = Button(janela, width = l, text = "1/X")
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=#
#Definição do posicionamento do botão com gerenciador PLACE.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=#
bt_pi.place(x = a, y = c1)
bt_zero.place(x = b, y = c1)
bt_point.place(x = c, y = c1)
bt_equal.place(x = d, y = c1)
bt_one.place(x = a, y = c2)
bt_two.place(x = b, y = c2)
bt_three.place(x = c, y = c2)
bt_plus.place(x = d, y = c2)
bt_four.place(x = a, y = c3)
bt_five.place(x = b, y = c3)
bt_six.place(x = c, y = c3)
bt_minus.place(x = d, y = c3)
bt_seven.place(x = a, y = c4)
bt_eigh.place(x = b, y = c4)
bt_nine.place(x = c, y = c4)
bt_times.place(x = d, y = c4)
bt_ce.place(x = a, y = c5)
bt_c.place(x = b, y = c5)
bt_back.place(x = c, y = c5)
bt_divide.place(x = d, y = c5)
bt_per.place(x = a, y = c6)
bt_raiz.place(x = b, y = c6)
bt_square.place(x = c, y = c6)
bt_div.place(x = d, y = c6)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
def labels_iniciais():
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=#
    #-=-=-=-=Definição dos Labels da calculadora.=--=-=#
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=#
    lb_one = Label(janela, text = "0" + " "*93)
    lb_two = Label(janela, text = "0" + " "*90)
    lb_three = Label(janela, text = "0" + " "*100)
    lb_operator = Label(janela, text = " ")
    lb_equal = Label(janela, text = " = ")

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=--=#
    #Definição do posicionamento dos Labels com gerenciador PLACE.
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    lb_one.place(x = a, y = margem_topo1)
    lb_two.place(x = a, y = margem_topo2)
    lb_three.place(x = a, y = margem_topo3)
    lb_operator.place(x = 300, y = margem_topo1)
    lb_equal.place(x = 295, y = margem_topo2)
labels_iniciais()
janela.mainloop()
