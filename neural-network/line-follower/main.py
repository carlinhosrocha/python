# rede neural para seguidor de linha com 3 sensores ópticos:
from random import randint
import math
# nn 3x3x3
# declaração de neurônios e pesos:
dados = [
	# frente [1, 1, 1]
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
	# frente [0, 0, 0]
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
	# frente [0, 1, 0]
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
	# esquerda [1, 0, 0]
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
	# esquerda [1, 1, 0]
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
	# direita [0, 0, 1]
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
	# direita [0, 1, 1]
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
# valores para treinamento supervisionado:
label = [
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[0, 1, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[1, 0, 0],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
	[0, 0, 1],
]

entrada = [1, 1, 1]
oculta = [0, 0, 0]
saida = [0, 0, 0]
pesos= [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
bias = 0
rate = 0.1
erro = 0
# função de inicialização dos pesos:
def iniciar():
	global pesos;
	for i in range(len(pesos)):
		for n in range(len(pesos[i])):
			for k in range(len(pesos[i][n])):
				pesos[i][n][k] = randint(0, 1000)/1000
# cálculo do valor dos neurônios:
def neuronios():
	global entrada, oculta, saida;
	# atualização dos neurônios da camada oculta:
	for i in range(len(oculta)):
		for n in range(len(entrada)):
			oculta[i] = oculta[i] + entrada[n] * pesos[0][i][n] + bias
		oculta[i] = sigmoide(oculta[i]) # 'regulando' valor do neurônio
	# atualização dos neurônios da camada de saída:
	for i in range(len(saida)):
		for n in range(len(oculta)):
			saida[i] = saida[i] + oculta[n] * pesos[1][i][n] + bias
		saida[i] = sigmoide(saida[i])
# função de ativação:
def sigmoide(x):
	return 1 / (1 + math.exp(-x))
# função de cálculo de erro:
def loss():
	global erro;
	for i in range(len(saida)):
		erro = target[i] - saida[i]
def weight():
	global pesos, entrada;
	# W1 = W1 + LearningRate * E * X1
	for i in range(len(pesos)):
		for n in range(len(pesos[i])):
			for k in range(len(pesos[i][n])):
				pesos[i][n][k] = pesos[i][n][k] + rate * erro * entrada[i]
# função de treinamento:
def treinamento(epoca):
	global entrada, target, erro;
	for i in range(epoca):
		for n in range(len(dados)):
			entrada = dados[n]
			target = label[n]
			neuronios() # atualiza o valor do neurônio
			loss() # calcula o valor do erro (perda)
			weight() # atualiza o valor dos pesos
			print(pesos[0])
			erro = 0
			

iniciar()
neuronios()
treinamento(5)

entrada = [1, 1, 0.1]
neuronios()
print(saida)