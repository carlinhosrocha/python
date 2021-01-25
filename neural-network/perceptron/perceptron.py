from random import randint
# ============================== #
# = Redes Neurais - PERCEPTRON = #
# ============================== #
# Receita do Perceptron:
# 1-Iniciar com um conjunto de dados supervisionados.       X1---|W1|-------+--------+
# 2-Feed Foward (Perceptron faz as predições).                        |	    |		 |
# 3-Calcular os erros (loss) e atualizar os pesos.                    | sum | step(n)|-----Y(predição)
# Repetir 2 e 3 para cada registro = Perceptron Rule.                 |     |		 |
# Declaração dos neurônios e pesos:                         X2---|W2|-------+--------+
X1 = None
X2 = None
W1 = 0
W2 = 0
Y = None
Ý = None
E = None
LearningRate = 0.1
Época = 5
# valores para treinamento:
# +----------+----+----+--------+
# + Registro + X1 + X2 + Target +
# +----------+----+----+--------+
# + Sit. A   + 0  + 0  +   0    +
# + Sit. B   + 0  + 1  +   1    +
# + Sit. C   + 1  + 0  +   1    +
# + Sit. D   + 1  + 1  +   1    +
# +----------+----+----+--------+
dados = (
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 1)
)
# Os pesos são inicializados aleatoriamente:
W1 = randint(0, 100) / 100 # valores de 0.00 à 1.00
W2 = randint(0, 100) / 100 # valores de 0.00 à 1.00
# Iniciando o Feed Foward:
# Y(predição) = g(w1*x1 + w2*x2) [g -> função degrau]
# Função degrau(ativação):
def degrau(z):
    if z >= 0.5:
        return 1
    else:
        return 0
# Função de predição:
def predição():
    global W1, W2, X1, X2; # acessando variáveis globais
    return degrau(W1*X1 + W2*X2)
# Função atualizar pesos:
def atualizar():
    global W1, W2, LearningRate, E, X1, X2; # acessando variáveis globais
    W1 = W1 + LearningRate * E * X1
    W2 = W2 + LearningRate * E * X2
# Treinamento:
for n in range(Época):
    for i in range(4):
        X1 = dados[i][0]
        X2 = dados[i][1]
        Y = dados[i][2]
        Ý = predição()
        E = Y - Ý
        atualizar() # atualizando os pesos
# Entrada do usuário:
X1 = int(input(f"Digite X1: "))
X2 = int(input(f"Digite X2: "))
print(f"Predição: {predição()}")