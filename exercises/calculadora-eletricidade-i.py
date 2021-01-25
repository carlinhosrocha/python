print("/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/")
print("///Calculadora de Eletricidade 1.0//")
print("/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/")
print("")
print("====================================")
print("=               MENU               =")
print("====================================")
print("--- Selecione qual lei/equação: ----")
print("------------------------------------")
print("[1] para cálculo de Força elétrica..")
print("[2] para cáculo de Tensão...........")
print("[3] para cálculo de Lei de Ohm......")
print("[4] para cálculo de Resistividade...")
print("[5] para cálculo de Condutância.....")
print("[6] para cálculo de Potência........")
print("------------------------------------")
print("")
escolha = int(input("Entre com a opção escolhida: "))
if (escolha == 1):
     k = (9*(10**9))#constante k 
     print("------------------------------------")
     print("-- CÁLCULO DE FORÇA ELETROSTÁTICA --")
     print("------------------------------------")
     print("=  QUAL É A INCÓGNITA DA EQUAÇÃO:   ")
     print("====================================")
     print("= [1] para FORÇA....................")
     print("= [2] para CARGA I..................")
     print("= [3] para CARGA II.................")
     print("= [4] para DISTÂNCIA................")
     print("====================================")
     incognita = int(input("Digite o número correspondente: "))
     if (incognita == 1):
          q1 = float(input("Digite o valor da carga de Q1 em coulombs: "))
          q2 = float(input("Digite o valor da carga de Q2 em coulombs: "))
          r = float(input("Digite o valor da distância entre as cargas em metros: "))
          #cálculo usando fórmula padrão
          forca = k*((q1*q2)/(r**2))
          print("O valor da Força é de: %.2f N." %(forca))
     if (incognita == 4):
          f = float(input("Digite o valor da força eletrostática:"))
          q1 = float(input("Digite o valor da carga de Q1 em coulombs: "))
          q2 = float(input("Digite o valor da carga de Q2 em coulombs: "))
          #fórmula obtida a partir de manipulação algébrica
          r = ((k*q1*q2)/f)**(1/2)
          print("O valor da distância em Metros é de: %.2f m." %(r))

saida = input("Click qualquer tecla para sair...")

     
     
          
     
     
