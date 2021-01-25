from random import shuffle
# entrada dos nomes
n1 = str(input('Digite o nome da primeira pessoa: '))
n2 = str(input('Digite o nome da segunda pessoa: '))
n3 = str(input('Digite o nome da terceira pessoa: '))
n4 = str(input('Digite o nome da quarte pessoa: '))
lista = [n1, n2, n3, n4]
# sorteando lista
shuffle(lista)
print(f'A ordem será : {lista}.')
