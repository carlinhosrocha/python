lista = [[],[]] #lista com duas sublistas 
for i in range(1, 8): #laço para a entrada de dados
    num = int(input(f'Digite o {i}° termo: ')) #entrada de valores
    if num % 2 == 0: #checa se o numero é par
        lista[0].append(num) #insere valor na sublista [0] da lista
    else: #se o numero não atende a primeira condição, logo atenderá a segunda
        lista[1].append(num) #insere valor na sublista [1] da lista
lista[0].sort() #organiza a lista de pares em ordem crescente
lista[1].sort()#organiza s lista de impares em ordem crescente
print('='*20) #exibe barra de separação
print(f'Os valores pares são {lista[0]}.') #exibe valores pares
print(f'Os valores impares são {lista[1]}.')#exibe valores impares
