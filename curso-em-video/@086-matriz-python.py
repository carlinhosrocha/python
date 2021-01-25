matriz = [[],[],[]] #matriz com três sublistas
for i in range(0, 3): #para as três listas
    for x in range(0, 3): #para os três elementos
        matriz[i].append(int(input(f'Digite o valor para [{i},{x}]: '))) #armazena os valores
print('='*27) #barra horizontal
for y in range(0, 3): #para as três listas
    for z in range(0, 3): #para os três termos
        print(f'[ {matriz[y][z]:^5} ]', end='') #exibe os valores em y - z com 5 espaços centralizados
    print() #quebra de linha
print('='*27) #barra horizontal
