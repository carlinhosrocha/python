from random import randint # função de sorteio aleatório
e = 2.7182818284590452353602874 # número de euler
# modelo simplificado de rede neural artifical, visando fixar os principais conceitos.
# objetivo da rede: balancear os pesos corretamente para que a saída seja correspondente a 1 ou 0.
entrada = ((0, 0, 0, 1), (1, 1, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0)) # dados de entrada para treinamento do modelo
# (e0, e1, s0, s1)
# camada de saída:
saida = [[], []]
# matriz de pesos:
peso = [[], [],] # pesos = [entrada0, entrada1,]
# função sigmoide (função de ativação):
def sigmoide(x):
    f = 1 / (1 + (e**x))
    if f < 0.5:
        return  0
    else:
        return 1
# função de inicialização:
def iniciar_pesos():
    # inicializando os pesos com valores aleatórios:
    for i in range(0, 2, 1):
        for n in range(0, 2, 1):
            x = randint(-10, 10)
            peso[i].append(x)
iniciar_pesos()
# calculando o valor de erro da saída:
def calculo_erro():
    erro = []
    error = 0
    k = 2
    for i in range(0, 4, 1):
        saida[0].append(sigmoide(entrada[i][0]*peso[0][0] + entrada[i][1]*peso[1][0]))
        saida[1].append(sigmoide(entrada[i][0]*peso[0][1] + entrada[i][1]*peso[1][1]))
    for m in range(0, 2, 1):
        for n in range(0, 4, 1):
            erro.append((saida[m][n] - entrada[n][k])**2)
        k=k+1
    for j in range(0, len(erro), 1):
        error = error + erro[j]
    return error
custo = calculo_erro()
# ajustando os pesos para um menor erro:
def ajustar_pesos():
    for i in range(0, 2, 1):
        for n in range(0, 2, 1):
            peso[i].insert(n, ajuste(peso[i][n], custo))
# função de ajuste dos pesos:
def ajuste(x, y):
    deri = 2 * custo * sigmoide(sum(saida)*2)
    print(deri)
ajustar_pesos()
"""
print(entrada)
print(saida)
print(peso)
print(custo)
"""