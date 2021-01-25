matriz = [[],[],[]] #matriz de valores
pares = 0 #números pares
terceira = 0 #terceira coluna
segunda = 0 #segunda linha
for i in range(0, 3): #três sublistas
    for c in range(0, 3): #três elementos
        matriz[i].append(int(input(f'Digite o elemento {[i, c]}: '))) #entrada de valores
        if matriz[i][c] % 2 == 0: #checa se elemento digitado é par
            pares += matriz[i][c]
        if c == 2: #terceira coluna
            terceira += matriz[i][c]
        if i == 1: #segunda linha
            segunda += matriz[i][c]
print('='*30) #barra horizontal
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matriz[x][y]:^5}]', end='')
    print()
print('='*30) #barra horizontal
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'A soma dos valores da segunda linha é {segunda}.')
