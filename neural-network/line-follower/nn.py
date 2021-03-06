import numpy as np
import math
from random import randint

data = [
	# frente [0.5]
	[0.910, 0.773, 0.844],
	[0.920, 0.755, 0.822],
	[0.995, 0.869, 0.866],
	[0.984, 0.795, 0.980],
	[0.775, 0.793, 0.999],
	[0.998, 0.848, 0.884],
	[0.800, 0.800, 0.977],
	[0.813, 0.957, 0.861],
	[0.753, 0.852, 0.912],
	[0.849, 0.891, 0.753],
	# frente [0.5]
	[0.079, 0.200, 0.174],
	[0.024, 0.094, 0.094],
	[0.039, 0.046, 0.138],
	[0.044, 0.135, 0.061],
	[0.031, 0.030, 0.128],
	[0.088, 0.080, 0.091],
	[0.193, 0.071, 0.175],
	[0.010, 0.149, 0.176],
	[0.035, 0.083, 0.193],
	[0.158, 0.100, 0.140],
	# frente [0.5]
	[0.130, 0.982, 0.108],
	[0.181, 0.950, 0.077],
	[0.045, 0.934, 0.076],
	[0.054, 0.807, 0.149],
	[0.178, 0.955, 0.031],
	[0.178, 0.923, 0.031],
	[0.121, 0.779, 0.038],
	[0.135, 0.811, 0.181],
	[0.146, 0.923, 0.169],
	[0.082, 0.886, 0.128],
	# esquerda [0]
	[0.910, 0.029, 0.145],
	[0.900, 0.030, 0.118],
	[0.956, 0.168, 0.130],
	[0.820, 0.174, 0.012],
	[0.882, 0.134, 0.016],
	[0.866, 0.129, 0.107],
	[0.932, 0.157, 0.159],
	[0.942, 0.001, 0.118],
	[0.979, 0.166, 0.075],
	[0.770, 0.156, 0.106],
	# esquerda [0]
	[0.980, 0.908, 0.158],
	[0.777, 0.922, 0.179],
	[0.932, 0.833, 0.047],
	[0.959, 0.876, 0.110],
	[0.827, 0.906, 0.104],
	[0.813, 0.918, 0.076],
	[0.976, 0.793, 0.149],
	[0.987, 0.781, 0.120],
	[0.764, 0.831, 0.100],
	[0.981, 0.984, 0.173],
	# direita [1]
	[0.043, 0.105, 0.901],
	[0.016, 0.172, 0.887],
	[0.151, 0.084, 0.958],
	[0.195, 0.194, 0.779],
	[0.002, 0.007, 0.925],
	[0.093, 0.157, 0.770],
	[0.013, 0.153, 0.880],
	[0.028, 0.147, 0.879],
	[0.088, 0.071, 0.870],
	[0.115, 0.045, 0.904],
	# direita [1]
	[0.153, 0.906, 0.993],
	[0.012, 0.995, 0.771],
	[0.067, 0.980, 0.934],
	[0.063, 0.876, 0.929],
	[0.035, 0.934, 0.974],
	[0.154, 0.912, 0.850],
	[0.164, 0.847, 0.869],
	[0.132, 0.844, 0.971],
	[0.113, 0.787, 0.848],
	[0.072, 1.000, 0.831],
]

labels = [
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.5],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0],
	[1.0]
]

def uniform(m, n): # fun????o que retorna valores float aleat??rios:
	return randint(m*1000, n*1000)/1000

# INICIALIZA????O DOS PESOS:
WXE1 = np.array([uniform(-1, 1) for i in range(4)]) # pesos primeiro neur??nio da camada de entrada
WXE2 = np.array([uniform(-1, 1) for i in range(4)]) # pesos segundo neur??nio da camada de entrada

WO1E = np.array([uniform(-1, 1) for i in range(2)]) # pesos primeiro neur??nio da camada oculta
WO2E = np.array([uniform(-1, 1) for i in range(2)]) # pesos segundo neur??nio da camada oculta

WS = np.array([uniform(-1, 1) for i in range(2)]) # pesos neur??nio da camada de sa??da

# CRIA????O DOS NEUR??NIOS DA REDE NEURAL:
X = None # dados para 'alimenta????o' da rede neural
E1 = None # primeiro neur??nio da camada de entrada
E2 = None # segundo neur??nio da camada de entrada
O1 = None # primeiro neur??nio da camada oculta
O2 = None # segundo neur??nio da camada oculta
S = 0 # valor da sa??da
B = 0.1 # valor da constante bias (vies)
custo = 0 # valor da taxa de custo
target = [] # valor dos dados para supervis??o

# CRIA????O DA FUN????O PRINCIPAL DA REDE NEURAL:
def redeNeural():
	global WXE1, WXE2, WO1E, WO2E, WS, X, S, custo # definindo as vari??veis como escopo global
	S = feedfoward() # recebe o valor da sa??da
	custo = target - S # c??lculo da taxa de custo
	atualizaPesos(custo) # backpropagation dos pesos

# ALGORITMO DE PROPAGA????O DOS DADOS PELA REDE:
def feedfoward():
	global WXE1, WXE2, WO1E, WO2E, WS, X, E1, E2, O1, O2, S; # definindo as vari??veis como escopo global

	E1 = tangenteHiperbolica(np.sum(X * WXE1)) # valor do primeiro neur??nio da camada de entrada
	E2 = tangenteHiperbolica(np.sum(X * WXE2)) # valor do segundo neur??nio da camada de entrada

	O1 = tangenteHiperbolica(np.sum(np.array([E1, E2]) * WO1E)) # valor do primeiro neur??nio da camada oculta
	O2 = tangenteHiperbolica(np.sum(np.array([E1, E2]) * WO2E)) # valor do segundo neur??nio da camada oculta

	resul = sigmoid(np.sum(np.array([O1, O2]) * WS)) # valor camada de saida

	return resul

# FUN????O DE ATIVA????O 1:
def tangenteHiperbolica(x):
	th = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
	return th

# FUN????O DE ATIVA????O 2:
def sigmoid(x):
	return 1 / (1 + np.exp(-x))

# ATUALIZA????O E AJUSTE DOS PESOS (MEM??RIA): 
def atualizaPesos(erro, alpha=0.001):
	global WXE1, WXE2, WO1E, WO2E, WS, X, E1, E2, O1, O2, S; # definindo as vari??veis como escopo global

	for i in range(len(WS)):
	    if i == 0:
	        entrada = O1 # primeiro neur??nio da camada oculta
	    elif i == 1:
	        entrada = O2 # sengundo neur??nio da camada oculta

	    WS[i] = WS[i] + (alpha * entrada * erro) # atualiza????o do peso

	for i in range(len(WO1E)):
	    if i == 0:
	        entrada1 = E1 # primeiro neur??nio da camada de entrada
	    if i == 1:
	        entrada1 = E2 # segundo neur??nio da camada de entrada

	    WO1E[i] = WO1E[i] + (alpha * entrada1 * erro) # atualiza????o do peso

	for i in range(len(WO2E)):
		if i == 0:
			entrada2 = E1 # primeiro neur??nio da camada de entrada
		if i == 1:
			entrada2 = E1 # segundo neur??nio da camada de entrada

		WO2E[i] = WO2E[i] + (alpha * entrada2 * erro) # atualiza????o do peso

	for i in range(len(WXE1)): # pesos do primeiro neur??nio de entrada
		WXE1[i] = WXE1[i] + (alpha * X[i] * erro) 

	for i in range(len(WXE2)): # pesos do segundo neur??nio de entrada
		WXE2[i] = WXE2[i] + (alpha * X[i] * erro)    

X1 = 0
X2 = 0
X3 = 0

# FASE DE TREINAMENTO:
for k in range(1000):
	for i in range(70):
		X1 = data[i][0]
		X2 = data[i][1]
		X3 = data[i][2]
		target = labels[i]
		X = np.array([X1, X2, X3, B])
		redeNeural()
	if(custo < 0.10):
		break
	print(custo)

# IMPLEMENTA????O DA REDE TREINADA:
X1 = float(input(f'X1: '))
X2 = float(input(f'X2: '))
X3 = float(input(f'X3: '))
X = np.array([X1, X2, X3, B])

print(feedfoward())