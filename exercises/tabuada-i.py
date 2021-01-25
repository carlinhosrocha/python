print("========================")
print("== TABUADA MATEMÁTICA ==")
print("========================")
print("")
multiplicador = 0
escolha = int(input("Escolha qual a tabuada de qual número: "))
fim = int(input("Agora digite até que número será exibida a tabuada: "))
while (multiplicador < fim):
     multiplicador += 1
     resultado = escolha * multiplicador
     print(escolha,"X", multiplicador,"=", resultado)
else:
     saida = input("Fim da tabuada. Click qualquer tecla para sair...")
