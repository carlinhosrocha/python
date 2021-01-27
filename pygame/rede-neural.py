# rede neural para reconhecimento de dígitos manuscritos do dataset MNIST
# foi usado o SGD (Stochastic Gradient Descent)
import random # biblioteca para gerar valores aleatórios
import numpy as np # importação da biblioteca numpy
# abaixo, classe principal da rede neural:
class Network(object):
    # construtor da classe:
    def __init__(self, sizes):
        self.num_layers = len(sizes) # quantidade de camadas
        self.sizes = sizes # tamanho
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]] # criação dos viéses
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])] # criação dos pesos
    # dado a entrada, é calculado a saída:
    def feedfoward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a
    # método SGD:
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        training_data = list(training_data) # lista de tuplas(x, y) com a entrada e saída correspondente
        # epochs -> n° de épocas
        # mini_batch_size -> tamanho dos mini lotes
        # eta -> taxa de aprendizagem
        # test_data -> exibe no console infos sobre o treinamento
        n = len(training_data)
        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta) # aplicasse o passo da descidda do gradiente
            if test_data:
                print("Epoch: {} : {} / {}".format(j, self.evaluate(test_data), n_test))
            else:
                print("Epoch {} finalizada".format(j))
    # atualização dos pesos e bias
    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in swlf.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y) # algoritmo de backpropagation
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch)*nw for w, nw in zip(self.weights, nabla_w))]
        self.biases = [b-(eta/len(mini_batch)*nb for b, nb in zip(self.biases, nabla_b))]
    # algoritmo de backpropagation (calcula o melhor gradiente)
    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedfoward:
        activation = x
        # lista para armazenar todas as ativações, camada por camada:
        activations = [x]
        # lista para armazenar todos os vetores z, camada por camada:
        zs = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs = append(z)
            activation = sigmoid(z)
            activations = append(activation)
        # backward pass:
        delta = self.cost_derivate(activations[-1, y]) * sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)
# rede = Network([2, 3, 1]) -> 1° camada: 2 neurônios, 2° camada: 3 neurônios, 3° camada: 1 neurônio
# função de ativação sigmoid:
def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))
