alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# chave de acesso
chave = 3
# mensagem a ser convertida
mensagem = input("Digite uma palavra para ser criptografada: ")
# 'padronizando' a mensagem 
mensagem = mensagem.lower()
# tamanho da lista alfabeto
n = len(alfabeto)
# variável para concatenação
cifrada = ""
# laço de criptografia
for letra in mensagem:
    # achar no alfabeto a letra que esteja chave posições a frente
    indice = alfabeto.index(letra)
    nova_letra = alfabeto[(indice + chave)%n]
    # substituir na mensagem a letra pela nova_letra
    cifrada = cifrada + nova_letra
# mensagem criptografa
print(mensagem)
print(cifrada)