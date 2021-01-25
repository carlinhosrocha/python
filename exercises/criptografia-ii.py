# módulo para gerar a chave aleatória
import random
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# chave de acesso aleatória
chave = random.randrange(1, 256, 1)
# mensagem a ser convertida
mensagem = input("Digite uma palavra para ser criptografada: ")
# 'padronizando' a mensagem 
mensagem = mensagem.lower()
# tamanho da tabela ASCII
n = 128
# variável para concatenação
cifrada = ""
# laço de criptografia
for letra in mensagem:
    # achar no alfabeto a letra que esteja chave posições a frente
    indice = ord(letra)
    nova_letra = chr((indice + chave)%n)
    # substituir na mensagem a letra pela nova_letra
    cifrada = cifrada + nova_letra
# mensagem criptografa
print("A chave de acesso é", chave)
print(cifrada)
