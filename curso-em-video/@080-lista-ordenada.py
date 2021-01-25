#------------------------------------ Solução Guanabara -------------------------------------------------#
numeros = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print(f'Os valores digitados foram {numeros}.')
