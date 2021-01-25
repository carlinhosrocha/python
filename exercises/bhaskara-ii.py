print("==========================")
print("  BHASKARA__CALCULATOR 2.0")
print("==========================")
print("")
a = int(input("Digite o valor de A: "))
b = int(input("Agora, digite o valor de B: "))
c = int(input("Por fim, digite o valor de C: "))
print("")
if (a == 1):
     if (b > 0) and (c > 0):
          print("===========================")
          print("A equação digitada é:")
          print( "X² +", b, "X +",c, " = 0")
          print("===========================")
     elif (b < 0) and (c > 0):
          print("==========================")
          print("A equação digitada é:")
          print( "X²", b, "X +",c, " = 0")
          print("==========================")
     elif (b < 0) and (c < 0):
          print("======================")
          print("A equação digitada é:")
          print( "X²", b, "X",c, " = 0")
          print("======================")
     elif (b > 0) and (c < 0):
          print("======================")
          print("A equação digitada é:")
          print( "X² +", b, "X",c, " = 0")
          print("======================")
else:
     if (b > 0) and (c > 0):
          print("===========================")
          print("A equação digitada é:")
          print( a,"X² +", b, "X +",c, " = 0")
          print("===========================")
     elif (b < 0) and (c > 0):
          print("==========================")
          print("A equação digitada é:")
          print( a,"X²", b, "X +",c, " = 0")
          print("==========================")
     elif (b < 0) and (c < 0):
          print("======================")
          print("A equação digitada é:")
          print( a,"X²", b, "X",c, " = 0")
          print("======================")
     elif (b > 0) and (c < 0):
          print("======================")
          print("A equação digitada é:")
          print( a,"X² +", b, "X",c, " = 0")
          print("======================")
#raízes da equação:
delta = ((b**2)-(4*a*c))
x1 = ((-b + (delta**(1/2)))/(2*a))
x2 = ((-b - (delta**(1/2)))/(2*a))
#fim do corpo-calculador.
print("")
print("..........................")
print("O valor de DELTA é: ", delta,".")
if (delta < 0):
     print("---------------------------------------------")
     print("NÃO HÁ SOLUÇÃO REAL PARA A EQUAÇÃO DIGITADA!!")
     print("---------------------------------------------")
elif (delta == 0):
     x = (-b)/(2*a)
     print("---------------------------------------------")
     print("A raíz da equação digitada é: X = %.2f" %(x))
     print("---------------------------------------------")
elif (delta > 0):
     print("----------------------------------------------------------")
     print("As raízes da equação digitada são: X¹ = %.2f e X² = %.2f." %(x1, x2))
     print("----------------------------------------------------------")
enter = input("Click ENTER para encerrar o programa!!!")
