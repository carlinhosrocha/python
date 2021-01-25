b = int(input("Digite o número da tabuada: "))
a = int(input("Digite até que número a tabuada será exibida: "))
for a in range(-1,a,1):
     a += 1
     c = a*b
     print(a,"X",b,"=",c)
saida = input("Click para sair...")
